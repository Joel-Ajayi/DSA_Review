"""
Coin Problem:
Given a set of coin values = {c1, c2...cn} and a target sum of money m, in how
many ways can we form the sum m using these coins

"""


def how_many_ways(m: int, coins: list[int]):
    dp = [0 for _ in range(m + 1)]

    # because because they is only one way to get cost of 0
    dp[0] = 1
    for c in range(1, m + 1):
        for coin in coins:
            if coin <= c:
                # since we are adding up to current coin capacity
                dp[c] += dp[c - coin]

    return dp[c]


coins = [1, 4, 5]
# --- Example ---
max_val = how_many_ways(5, coins)
print(f"Maximum number of ways: {max_val}")
