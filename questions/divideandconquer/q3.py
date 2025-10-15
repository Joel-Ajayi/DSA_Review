"""
A robber goes from house to house to rob

constraint: Cannot rob adjacent building
ouput: max robbery ammount
"""


def house_robber_tb(n: int, houses: list[int], memo: dict[int, int] = {}):
    if n < 1:
        return 0
    if n == 1:
        return houses[0]
    if n == 2:
        return max(houses[0], houses[1])

    if n not in memo:
        curr = houses[n - 1]
        prev_2 = house_robber_tb(n - 2, houses)
        prev_1 = house_robber_tb(n - 1, houses)
        memo[n] = max(curr + prev_2, prev_1)

    return memo[n]


# greedy algo
def house_robber_bt(houses: list[int]):
    robbed_houses = [0] * len(houses)
    robbed_houses[0] = houses[0]
    robbed_houses[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        robbed_houses[i] = max(robbed_houses[i - 2] + houses[i], robbed_houses[i - 1])

    return robbed_houses[-1]


street = [6, 7, 1, 30, 8, 2, 4]
print(f"Maximum loot: {house_robber_bt(street)}")
print(f"Maximum loot: {house_robber_tb(7, street)}")
