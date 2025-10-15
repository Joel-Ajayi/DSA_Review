"""
Given a set of items, each with weight and value,
determine the number of each item to include in a collection,
so that the total weight is less than or equal to a given
limit and the total value is as large as possible
"""

items = [(20, 100), (30, 120), (10, 60)]


def knapsack():
    sorted_items = sorted(items, key=lambda item: item[1] / item[0], reverse=True)
    i = 0
    kg_limit = 50
    remaining_kg = 50
    total_val = 0

    i = 0
    while remaining_kg > 0 and i < len(sorted_items):
        kg = sorted_items[i][0]
        val = sorted_items[i][1]
        if kg <= remaining_kg:
            remaining_kg -= kg
            total_val += val
        else:
            total_val += remaining_kg * (val / kg)
            remaining_kg = 0

        i += 1

    print("Total value : ", total_val)
    print("Total kg : ", kg_limit, " and remaining: ", remaining_kg)


knapsack()
