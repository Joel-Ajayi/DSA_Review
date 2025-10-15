"""
Knapsack Problem
"""


def knapsack(n: int, c: int, arr: list[tuple[int, int]], tracker: dict[int, int] = {}):

    if n > len(arr) or c <= 0 or arr[n - 1][0] > c:
        return 0

    val = arr[n - 1]
    # if not n in tracker:
    # do not take current val
    option1 = knapsack(n + 1, c, arr, tracker)
    # take current val
    option2 = val[1] + knapsack(n + 1, c - val[0], arr, tracker)
    ans = max(option1, option2)

    return ans


item_values = [60, 100, 50]
item_weights = [10, 20, 30]
items = list(zip(item_weights, item_values))
knapsack_capacity = 50
print(knapsack(1, c=knapsack_capacity, arr=items))


# With greedy Algo
def zero_one_knapsack(values, weights, capacity):
    num_items = len(values)
    # Create the DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(num_items + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):
            # item_index is i-1 because our items are 0-indexed
            item_index = i - 1

            # If the current item's weight is more than the current capacity w,
            # we can't include it.
            if weights[item_index] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Find the maximum of two choices:
                # 1. Don't include the item
                # 2. Include the item
                value_if_not_included = dp[i - 1][w]
                value_if_included = (
                    values[item_index] + dp[i - 1][w - weights[item_index]]
                )

                dp[i][w] = max(value_if_not_included, value_if_included)

    return dp[num_items][capacity]


# --- Example ---
max_val = zero_one_knapsack(item_values, item_weights, knapsack_capacity)
print(f"Maximum value in knapsack: {max_val}")
# Expected Output: Maximum value in knapsack: 220 (from items with value 100 and 120)
