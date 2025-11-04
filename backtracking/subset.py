#
# Each time you append a subset you call currSet.copy(), which is O(n) in the worst case.
# So generating and copying all subsets is O(n * 2^n), which dominates the sort.


# Time: O(n * 2^n)
def uniqueSubSets(nums: list[int]):
    nums.sort()
    currSet, subsets = [], []

    helper(0, nums, currSet, subsets)
    return subsets


def helper(i, nums: list[int], currSet: list[int], subsets: list[list[int]]):
    n = len(nums)
    if i >= n:
        subsets.append(currSet.copy())
        return

    # Decision one to include nums[i]
    currSet.append(nums[i])
    helper(i + 1, nums, currSet, subsets)
    currSet.pop()

    # For duplicate cases, since we do not want to repeat values
    while i + 1 < n and nums[i] == nums[i + 1]:
        i += 1

    # Decision to not include nums[i]
    helper(i + 1, nums, currSet, subsets)


res = uniqueSubSets([1, 2, 3])
print(res)
