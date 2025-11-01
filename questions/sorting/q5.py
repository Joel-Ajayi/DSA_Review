def cal(modules: list[int], memo={}):
    max_prev = 0
    n = len(modules)

    # the min of each group combination is usually the smallest value
    modules.sort()

    for d1i in range(n - 2):
        # |d1 - d2| + |d2 - d3| == d3 - d1 for sorted array
        d3i = d1i + 2
        ans = abs(modules[d1i] - modules[d3i])
        max_prev = max(max_prev, ans)

    return max_prev


print(cal([1, 2, 5, 3, 5]))


# def cal2(modules: list[int], memo={}):
#     max_prev = float("inf")
#     n = len(modules)

#     # the min of each group combination is usually the smallest value
#     modules.sort()

#     for d1i in range(n):
#         # |d1 - d2| + |d2 - d3| == d3 - d1 for sorted array
#         d2i = d1i + 1
#         if d2i > n - 1:
#             d2i = n - (d1i + 1)

#         d3i = d1i + 2
#         if d3i > n - 1:
#             d3i = n - (d1i + 2)

#         ans = abs(modules[d1i] - modules[d2i]) + abs(modules[d2i] - modules[d3i])
#         max_prev = min(max_prev, ans)

#     return max_prev


# print(cal2([1, 6, 8, 12, 16]))

# def taskAllocator(s: str):
#     cols = len(s)
#     rows = len(set(s))
#     dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

#     for i in range(1, rows + 1):
#         for j in range(1, cols + 1):
#             if s[i - 1] == s[j - 1]:
#                 # Not an operation so just use previous count
#                 dp[i][j] = dp[i - 1][i - j]
#             else:
#                 # Decisions
#                 # Remove the task from the string
#                 op1 = 1 + dp[i][j - 1]

#                 # append the task an assign to this server
#                 op2 = 1 + dp[i - 1][j]

#                 dp[i][j] = min(op1, op2)
#     print(dp)
#     return dp[rows][cols]


# print(taskAllocator("xzyzxa"))

# def taskAllocator(s: str):
#     char_freq = {}
#     count_freq = {}
#     for char in s:
#         # basically stores freq of each character
#         # frequency of each character count

#         prev_count = char_freq.get(char, 0)
#         new_count = prev_count + 1

#         char_freq[char] = prev_count + 1

#         prev_count_freq = count_freq.get(prev_count, 0)

#         count_freq[prev_count] = 0 if prev_count_freq == 0 else prev_count_freq - 1

#         if count_freq[prev_count] == 0:
#             del count_freq[prev_count]

#         count_freq[new_count] = count_freq.get(new_count, 0) + 1

#     global_ops = float("inf")
#     for target in count_freq.keys():
#         local_ops = 0

#         for freq, count in count_freq.items():
#             operations = abs((target - freq)) * count
#             local_ops += operations

#         global_ops = min(global_ops, local_ops)

#     return global_ops


# print(taskAllocator("xzyzxa"))

# import math


# def getMinimumCost(k, c: list):
#     c.sort(reverse=True)
#     costs = 0
#     for i, price in enumerate(c):
#         loop = (i // k) + 1

#         costs += loop * price

#     return costs


# print(getMinimumCost(3, [1, 3, 5, 7, 9]))
