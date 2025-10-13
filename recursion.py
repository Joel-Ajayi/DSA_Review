# def fibonacci(n: int):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# def factorial(n: int) -> int:
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def findMaxofArr(n, arr: list[int]):
#     if n == 1:
#         return arr[0]
#     return max(arr[-1], findMaxofArr(n - 1, arr))


# print([fibonacci(i) for i in range(4)])
# print(factorial(4))
# print(findMaxofArr(4, [fibonacci(i) for i in range(4)]))


# using memoization(top to bottom approach)
# f6 -> f5 -> f4 -> ...
def memoized_fib(n: int, memo: dict[int, int] = {}):
    if n <= 0:
        return 0

    if n == 1:
        return 1

    if not n in memo:
        memo[n] = memoized_fib(n - 1, memo) + memoized_fib(n - 2, memo)
    print(memo)
    return memo[n]


# using memoization(bottom to top approach)
# f(0) -> f(1) -> f(2) -> f(3)
def memoized_fib2(n: int):
    last_2, last_1, sum = 0, 1, 0

    for i in range(2, n + 1):
        sum = last_1 + last_2
        last_2 = last_1
        last_1 = sum

    return sum


print(memoized_fib2(7))
