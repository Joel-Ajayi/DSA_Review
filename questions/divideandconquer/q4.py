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
