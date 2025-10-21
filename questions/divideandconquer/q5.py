"""
Knapsack Problem
"""


def knapsack(
    currentIndex: int,
    capacity: int,
    items: list[tuple[int, int]],
    tempDict: dict[int, int] = {},
):

    if (
        currentIndex > len(items)
        or capacity <= 0
        or items[currentIndex - 1][0] > capacity
    ):
        return 0

    val = items[currentIndex - 1]
    # Decisions
    # 1.    do not take current val.
    #       No decrement in capacity
    # 2.    take current val

    option1 = knapsack(currentIndex + 1, capacity, items, tempDict)
    #
    option2 = val[1] + knapsack(currentIndex + 1, capacity - val[0], items, tempDict)

    ans = max(option1, option2)

    return ans


item_values = [60, 100, 50]
item_weights = [10, 20, 30]
items = list(zip(item_weights, item_values))
knapsack_capacity = 50
print(knapsack(1, capacity=knapsack_capacity, items=items))


# With greedy Algo
def zero_one_knapsack(
    values,
    weights,
    capacity,
):
    tempDict: dict[tuple[int, int], int] = {}
    num_items = len(values)
    # Create the DP table

    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                tempDict[(i, w)] = tempDict.get((i - 1, w), 0)
                continue

            # Do not pick the current item
            # Hence just use the prev max value
            option1 = tempDict.get((i - 1, w), 0)
            # subtract from the current capacity
            option2 = values[i - 1] + tempDict.get((i - 1, w - weights[i - 1]), 0)

            tempDict[(i, w)] = max(option1, option2)

    return tempDict[(num_items, capacity)]


# --- Example ---
max_val = zero_one_knapsack(item_values, item_weights, knapsack_capacity)
print(f"Maximum value in knapsack: {max_val}")
# Expected Output: Maximum value in knapsack: 220 (from items with value 100 and 120)
