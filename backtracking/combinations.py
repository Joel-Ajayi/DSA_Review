def combinations(nums: list[int]):
    nums.sort()
    currSet, subsets = [], []
    k = 2

    helper(0, nums, currSet, subsets, k)
    return subsets


# Time O(k * C(n, k))
def helper(i, nums: list[int], currComb: list[int], subsets: list[list[int]], k):
    if len(currComb) == k:
        subsets.append(currComb.copy())
        return

    n = len(nums)
    if i >= n:
        return

    # Decision one to include nums[i]
    for j in range(i, n):
        currComb.append(nums[j])
        # go to next value
        helper(j + 1, nums, currComb, subsets, k)
        currComb.pop()


res = combinations([1, 2, 3, 4, 5])
print(res)
