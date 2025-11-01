"""
Min cost to reach last cell
Constraint: You can only go right and down

"""


def min_cost(
    cost_arr: list[list[int]],
):
    n, m = len(cost_arr), len(cost_arr[0])
    dp = [float("inf")] * (m + 1)

    dp[1] = cost_arr[0][0]
    for i in range(1, n + 1):
        new_dp = [float("inf")] * (m + 1)
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                new_dp[j] = cost_arr[0][0]
                continue

            # current position depends on [i][j-1] or [i-1][j]
            # down movement
            op1 = dp[j]
            # right movement
            op2 = new_dp[j - 1]
            # down movement
            new_dp[j] = cost_arr[i - 1][j - 1] + min(op1, op2)
        dp = new_dp

    return dp[m]


matrix_2d = [
    [4, 7, 8, 6, 4],
    [6, 7, 3, 9, 2],
    [3, 8, 1, 2, 4],
    [7, 1, 7, 3, 7],
    [2, 9, 8, 9, 3],
]

# print(f"Min cost2D is: {min_cost(matrix_2d)}")


"""
Number of paths to reach last cell with given cost
Constraint: 
    1. You can only go right and down
    2. We are given total cost to reach end of matrix with "total cost"
    3. Find the number of ways to reach the end of matrix with the given cost
"""


def num_paths(cost_arr: list[list[int]], max_cost: int):
    n, m = len(cost_arr), len(cost_arr[0])
    dp = [[0] * (max_cost + 1) for _ in range(m + 1)]

    # base case
    start_cost = cost_arr[0][0]
    for i in range(1, n + 1):
        new_dp = [[0] * (max_cost + 1) for _ in range(m + 1)]
        for j in range(1, m + 1):
            cost = cost_arr[i - 1][j - 1]
            for c in range(cost, max_cost + 1):
                if j == 1 and i == 1:
                    new_dp[1][start_cost] = 1
                    continue

                # current position depends on [i][j-1] or [i-1][j]
                # down movement at this cost
                down_mov = dp[j][c - cost]
                # right movement
                right_mov = new_dp[j - 1][c - cost]

                # down movement
                new_dp[j][c] = down_mov + right_mov

        dp = new_dp

    return dp[m][max_cost]


matrix_2d2 = [
    [4, 7, 1, 6],
    [5, 7, 3, 9],
    [3, 2, 1, 2],
    [7, 1, 6, 3],
]


print(num_paths(matrix_2d2, 25))
