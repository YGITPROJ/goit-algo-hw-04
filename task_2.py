def merge_two_lists(a, b):
    result = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result


def merge_k_lists(lists):
    if not lists:
        return []

    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            left = lists[i]
            right = lists[i + 1] if i + 1 < len(lists) else []
            merged.append(merge_two_lists(left, right))

        lists = merged

    return lists[0]

def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)


if __name__ == "__main__":
    main()