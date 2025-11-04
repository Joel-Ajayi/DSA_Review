"""
For strings s1 and s2
covert s2 to s1 using delete, insert and replace operations
Find the minimum count of edit operations
"""


def convert_bt(
    s1: str,
    s2: str,
):
    len1, len2 = len(s1), len(s2)
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    # row - s1
    # col - s2

    # Base cases
    # when s2 is emtpy
    # Cost of inserting all of s1 to get an empty s2
    for i in range(len1 + 1):
        dp[i][0] = i

    # when s1 is empty
    # Cost of deleting all of s2 to get empty s1
    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            # when characters match
            if s1[i - 1] == s2[j - 1]:
                #  no operation is needed, so the cost is just the cost of
                # the subproblem before these characters.
                dp[i][j] = dp[i - 1][j - 1]
                continue

            # when you are inserting into s2, move s1 index to next
            # f(index1+1, index2) for recursion or (index1, index2-1) for table
            insert_op = dp[i][j - 1]

            # when you are deleting current value of s1, move s2 index to next
            # f(index1, index2+1) for recursion or (index1-1, index2) for table
            delete_op = dp[i - 1][j]

            # when you are replacing current value of s2 with s1
            # f(index1, index2) for recursion or f(index1-1, index2-1) for table
            replace_op = dp[i - 1][j - 1]

            dp[i][j] = 1 + min([insert_op, delete_op, replace_op])

    return dp[len1][len2]
