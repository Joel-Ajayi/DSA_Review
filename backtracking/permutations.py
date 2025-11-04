# e.g [1,2,3,4]

#   1       2     3      4      []
# -->    -->     -->   --->  --->
#           [2,3,4]       [3,4] <--- [4] <---
#           [3,2,4]  <--- [4,3]
# Finish <--[3,4,2]
#   it      [2,4,3]
#           [4,2,3]
#           [4,3,2]


def permutationRecursive(i, nums: list[int]):
    if i == len(nums):
        return [[]]

    resPerms = []
    # get to last value first
    perms = permutationRecursive(i + 1, nums)
    # Decision one to include nums[i]
    for p in perms:
        # O(n) work (copying/inserting lists)
        for j in range(len(p) + 1):
            pCopy = p.copy()
            pCopy.insert(j, nums[i])
            resPerms.append(pCopy)
    return resPerms


# Time O(n · n!) and O(n^2.n!) in worst case
res = permutationRecursive(0, [1, 2, 3, 4, 5])
print(len(res))


# Using Iteration
# Time O(n^2 . n!)
def permutationIterative(nums: list[int]):
    perms: list[list[int]] = [[]]

    for n in nums:
        new_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, n)
                new_perms.append(pCopy)

        perms = new_perms

    return perms


res = permutationIterative([1, 2, 3])
print(res)
