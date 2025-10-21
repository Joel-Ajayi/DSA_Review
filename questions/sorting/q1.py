def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return (0, arr)

    mid = n // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_swaps, left = merge_sort(left_arr)
    right_swaps, right = merge_sort(right_arr)

    # merge and count invertions
    l = len(left)
    r = len(right)

    li = 0
    ri = 0
    new_arr = []
    swaps_count = left_swaps + right_swaps

    while li < l and ri < r:
        new_index = len(new_arr) - 1

        if left[li] <= right[ri]:
            new_arr.append(left[li])
            li += 1
        else:
            new_arr.append(right[ri])
            swaps_count += l - li
            ri += 1

    new_arr.extend(left[li:])
    new_arr.extend(right[ri:])

    return swaps_count, new_arr


def countInversions(arr):
    swaps_count, sorted_arr = merge_sort(arr)
    return swaps_count


print(countInversions([7, 5, 3, 1]))
