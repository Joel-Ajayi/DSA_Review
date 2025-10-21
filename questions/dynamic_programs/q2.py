def countTriplets(arr: list[int], r):
    global_count = 0
    memo_right = {}
    memo_left = {}

    for x in arr:
        memo_right[x] = memo_right.get(x, 0) + 1
        memo_left[x] = memo_left.get(x, 0)

    for x in arr:
        memo_right[x] -= 1

        is_mid = x % r == 0
        if is_mid:
            a, c = x // r, x * r
            a_count = memo_left.get(a, 0)
            c_count = memo_right.get(c, 0)
            count = a_count * c_count
            global_count += count

        memo_left[x] += 1

    return global_count


my_arr = [1, 3, 9, 9, 27, 81]
# [1, 5, 5, 25, 125]
# r=3

# r=5
# [1, 3, 9, 9, 27, 81]

ratio = 3
print(countTriplets(my_arr, ratio))
