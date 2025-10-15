"""
Number factor problem
"""


def number_factor_top_bottom(n: int, count=0):
    if n in (0, 1, 2):
        return 1
    if n == 3:
        return 2
    if n < 0:
        return 0

    sub1 = number_factor_top_bottom(n - 1)
    sub2 = number_factor_top_bottom(n - 3)
    sub3 = number_factor_top_bottom(n - 4)

    return sum([sub1, sub2, sub3])


# ways(0) -> 1 (The only way is an empty set)

# ways(1) -> 1 (Just 1)

# ways(2) -> 1 (Only 1 + 1)

# ways(3) -> 2 (1+1+1 and 3)

# If n is negative -> 0 (Impossible)


def number_factor_bottom_top(n: int, count=0):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = dp[2] = 1
    dp[3] = 2

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]

    return dp[n]


print(number_factor_top_bottom(5))
print(number_factor_bottom_top(5))
