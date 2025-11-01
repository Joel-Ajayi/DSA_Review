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
knapsack_capacity = 30
print(knapsack(1, capacity=knapsack_capacity, items=items))
