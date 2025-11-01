"""
Min cost to reach last cell
Constraint: You can only go right and down

"""


def min_cost(
    arr: list[list[int]],
    row: int,
    col: int,
    memo: dict[tuple[int, int], int] = {},
):
    if row == 0 and col == 0:
        return arr[0][0]

    if row < 0 or col < 0:
        return float("inf")

    if (row, col) in memo:
        return memo[(row, col)]

    # decisions from bottom of array
    # 1. Move left
    # 2. Move up
    opt1 = min_cost(arr, row, col - 1, memo)
    opt2 = min_cost(arr, row - 1, col, memo)
    res = arr[row][col] + min(opt1, opt2)
    memo[(row, col)] = res
    return res


"""
Number of paths to reach last cell with given cost
Constraint: 
    1. You can only go right and down
    2. We are given total cost to reach end of matrix with "total cost"
    3. Find the number of ways to reach the end of matrix with the given cost
"""


def num_paths(
    arr: list[list[int]],
    max_cost: int,
    row: int,
    col: int,
    memo: dict[tuple[int, int, int], int] = {},
):

    cost = arr[row][col]
    key = (row, col, max_cost)

    if key in memo:
        return memo[key]

    if max_cost < 0:
        return 0

    if cost > max_cost:
        return 0

    # A path is formed when it gets to (0,0)
    # And uses exactly the specifc cost
    if row == 0 and col == 0:
        return 1 if cost == max_cost else 0

    # decisions from bottom of array
    # 1. Move left
    # 2. Move up
    # If we are on the first row, we can only come from the left
    if row == 0:
        result = num_paths(arr, max_cost - cost, row, col - 1, memo)
    # If we are on the first column, we can only come from above
    elif col == 0:
        result = num_paths(arr, max_cost - cost, row - 1, col, memo)
    else:
        opt1 = num_paths(arr, max_cost - cost, row, col - 1, memo)
        opt2 = num_paths(arr, max_cost - cost, row - 1, col, memo)
        result = opt1 + opt2

    memo[key] = result
    return memo[key]


matrix_2d = [
    [4, 7, 8, 6, 4],
    [6, 7, 3, 9, 2],
    [3, 8, 1, 2, 4],
    [7, 1, 7, 3, 7],
    [2, 9, 8, 9, 3],
]

matrix_2d2 = [
    [4, 7, 1, 6],
    [5, 7, 3, 9],
    [3, 2, 1, 2],
    [7, 1, 6, 3],
]

n = len(matrix_2d)
n2 = len(matrix_2d2)
print(num_paths(matrix_2d2, 25, n2 - 1, n2 - 1))
print(min_cost(matrix_2d, n - 1, n - 1))
