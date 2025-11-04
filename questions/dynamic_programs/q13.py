"""
Longest Palindromic Subsequence

"""


# Space: O(n). Time O(n^2)
def helper(lenght, l, r, s):
    n = len(s)
    while l >= 0 and r < n and s[l] == s[r]:
        lenght = max(r - l + 1, lenght)
        l -= 1
        r += 1
    return lenght


def lps(s: str):
    lenght = 0
    n = len(s)

    for i in range(n):
        #   even case
        lenght = helper(lenght, i, i + 1, s)

        # odd case
        lenght = helper(lenght, i, i, s)

    return lenght


print(lps("abaab"))
