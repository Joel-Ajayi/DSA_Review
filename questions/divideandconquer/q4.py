"""
For strings s1 and s2
covert s2 to s1 using delete, insert and replace operations
Find the minimum count of edit operations
"""


def convert_tb(
    s1: str,
    s2: str,
    index1: int = 0,
    index2: int = 0,
    memo: dict[tuple[int, int], int] = {},
):
    key = (index1, index2)
    if key in memo:
        return memo[key]

    # remaning number of s2 str to delete
    # when no s1 to perform any action
    if index1 == len(s1):
        return len(s2) - index2

    # remaining number of s1 to insert into s2
    # when no s2 to perform any action
    if index2 == len(s2):
        return len(s1) - index1

    # when characters match
    if s1[index1] == s2[index2]:
        # no count since no edit operation
        res = convert_tb(s1, s2, index1 + 1, index2 + 1)
    else:
        # when you are deleting current value of s2, move s2 index to next
        # f(index1, index2+1)
        delete_op = convert_tb(s1, s2, index1, index2 + 1)

        # when you are inserting into s2, move s1 index to next
        # f(index1+1, index2)
        insert_op = convert_tb(s1, s2, index1 + 1, index2)
        # when you are replacing current value of s2 with s1
        # typically f(index1, index2)
        # but increase index1 and index2 to avoid recorsion
        replace_op = convert_tb(s1, s2, index1 + 1, index2 + 1)

        res = 1 + min(delete_op, insert_op, replace_op)

    memo[key] = res
    return res


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
            else:
                # when you are inserting into s2, move s1 index to next
                # f(index1+1, index2) for recursion or (index1, index2-1) for table
                insert_op = dp[i][j - 1]

                # when you are deleting current value of s2, move s2 index to next
                # f(index1, index2+1) for recursion or (index1-1, index2) for table
                delete_op = dp[i - 1][j]

                # when you are replacing current value of s2 with s1
                # f(index1, index2) for recursion or f(index1-1, index2-1) for table
                replace_op = dp[i - 1][j - 1]

                dp[i][j] = 1 + min([insert_op, delete_op, replace_op])

    return dp[len1][len2]


def convert_bt_dict(s1: str, s2: str, tempDict: dict[tuple[int, int], int] = {}):
    len1, len2 = len(s1), len(s2)

    # row - s1
    # col - s2

    # Base cases
    # when s2 is emtpy
    # Cost of inserting all of s1 to get an empty s2
    for i in range(len1 + 1):
        key = (i, 0)
        tempDict[key] = i

    # when s1 is empty
    # Cost of deleting all of s2 to get empty s1
    for j in range(len2 + 1):
        key = (0, j)
        tempDict[key] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            tempDict.setdefault((i, j), 0)
            # when characters match
            if s1[i - 1] == s2[j - 1]:
                #  no operation is needed, so the cost is just the cost of
                # the subproblem before these characters.
                tempDict[(i, j)] = tempDict[(i - 1, j - 1)]
            else:
                # when you are inserting into s2, move s1 index to next
                # f(index1+1, index2) for recursion or (index1, index2-1) for table
                insert_op = tempDict[(i, j - 1)]

                # when you are deleting current value of s2, move s2 index to next
                # f(index1, index2+1) for recursion or (index1-1, index2) for table
                delete_op = tempDict[(i - 1, j)]

                # when you are replacing current value of s2 with s1
                # f(index1, index2) for recursion or f(index1-1, index2-1) for table
                replace_op = tempDict[(i - 1, j - 1)]

                tempDict[(i, j)] = 1 + min([insert_op, delete_op, replace_op])

    return tempDict[(len1, len2)]


print(convert_bt("tab", "tbrlt"))
print(convert_bt_dict("tab", "tbrlt"))
print(convert_tb("tab", "tbrlt"))
