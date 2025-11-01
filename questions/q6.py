import math


def collectMax(routes: list[list]):
    n = len(routes)
    m = len(routes[0])

    grid = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    count = 0
    i = 0
    j = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if routes[i][j] == -1:
                grid[i][j] = int(-math.inf)
            elif routes[i][j] == 0:
                grid[i][j] = grid[i - 1][j - 1]


routes = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]

print(collectMax(routes))
