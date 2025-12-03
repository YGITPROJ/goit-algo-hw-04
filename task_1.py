import timeit
import random
from functools import wraps


# Декоратор для заміру часу
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        execution_time = timeit.timeit(lambda: func(*args, **kwargs), number=1)
        return execution_time

    return wrapper


# Сортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


# Сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


@measure_time
def run_insertion(data):
    insertion_sort(data)


@measure_time
def run_merge(data):
    merge_sort(data)


@measure_time
def run_timsort(data):
    sorted(data)


def main():
    # Розміри наборів даних
    sizes = [100, 1000, 5000]

    print(
        f"{'Size':<10} | {'Insertion (s)':<15} | {'Merge (s)':<15} | {'Timsort (s)':<15}"
    )
    print("-" * 65)

    for size in sizes:
        original_data = [random.randint(0, 1000) for _ in range(size)]

        time_ins = run_insertion(original_data[:])
        time_mer = run_merge(original_data[:])
        time_tim = run_timsort(original_data[:])

        print(f"{size:<10} | {time_ins:<15.5f} | {time_mer:<15.5f} | {time_tim:<15.5f}")


if __name__ == "__main__":
    main()
