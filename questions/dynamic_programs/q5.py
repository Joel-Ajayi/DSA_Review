"""
Knapsack Problem
"""


# With dynamic programming
def zero_one_knapsack(
    values,
    weights,
    capacity,
):
    num_items = len(values)
    # Create the DP table

    dp = [[0 for _ in range(capacity + 1)] for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):
            item_weight = weights[i - 1]

            # if item weight is creater than current capacity
            # use count of previous item at this weight
            if item_weight > w:
                dp[i][w] = dp[i - 1][w]
                continue

            # Do not pick the current item
            # Hence just use the prev max value
            option1 = dp[i - 1][w]
            # subtract from the current capacity
            option2 = values[i - 1] + dp[i - 1][w - weights[i - 1]]

            dp[i][w] = max(option1, option2)

    return dp[num_items][capacity]


item_values = [60, 100, 50]
item_weights = [10, 20, 30]
items = list(zip(item_weights, item_values))
knapsack_capacity = 30

# --- Example ---
max_val = zero_one_knapsack(item_values, item_weights, knapsack_capacity)
print(f"Maximum value in knapsack: {max_val}")
# Expected Output: Maximum value in knapsack: 220 (from items with value 100 and 120)
