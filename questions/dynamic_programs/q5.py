"""
Knapsack Problems: 0/1 and Unbounded
"""


# With dynamic programming
def zero_one_knapsack(
    profit,
    weights,
    capacity,
):
    num_items = len(profit)
    # Create the DP table

    dp = [0] * (capacity + 1)
    for i in range(num_items):
        for w in range(1, capacity + 1):
            # Options 1: skip the current item
            # Hence just use the prev max value
            skip = dp[w]
            include = 0

            # Options 2: Subtract from the current capacity to get the new capacity
            if w - weights[i] >= 0:
                include = profit[i - 1] + dp[w - weights[i]]

            dp[w] = max(skip, include)

    return dp[-1]


# Given a list of N items, and a backpack with a limited capacity, return the maximum total
# profit that can be contained in the backpack. The i-th item's profit is profit[i]
# and it's wight is wight[i]. Assume you can have an unlimited number of each item available


def unbounded_knapsack(
    profit,
    weights,
    capacity,
):
    num_items = len(profit)
    # Create the DP table

    dp = [0] * (capacity + 1)

    for i in range(num_items):
        new_dp = [0] * (capacity + 1)
        for w in range(1, capacity + 1):
            # Options 1: skip the current item
            # Hence just use the prev max value
            skip = dp[w]
            include = 0

            # consider taking one more copy of item i (use new_dp to allow
            # repeated usage of the same item in this row)
            if w - weights[i] >= 0:
                include = profit[i] + new_dp[w - weights[i]]

            new_dp[w] = max(skip, include)

        dp = new_dp

    return dp[-1]


print(zero_one_knapsack(profit=[60, 100, 50], weights=[10, 20, 30], capacity=30))
print(zero_one_knapsack(profit=[4, 4, 7, 1], weights=[5, 2, 3, 1], capacity=8))
print(unbounded_knapsack(profit=[4, 4, 7, 1], weights=[5, 2, 3, 1], capacity=8))
