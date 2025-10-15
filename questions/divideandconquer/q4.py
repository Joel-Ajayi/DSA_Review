"""
For strings s1 and s2
covert s2 to s1 using delete, insert and replace operations
Find the minimum count of edit operations
"""


def convert_ub(s1: str, s2: str, index1: int = 0, index2: int = 0):
    # remaning number of s2 str to delete
    if index1 == len(s1):
        return len(s2) - index2

    # remaining number of s1 to insert into s2
    if index2 == len(s2):
        return len(s1) - index1

    if s1[index1] == s2[index2]:
        return convert_ub(s1, s2, index1 + 1, index2 + 1)

    delete_op = 1 + convert_ub(s1, s2, index1, index2 + 1)
    insert_op = 1 + convert_ub(s1, s2, index1 + 1, index2)
    replace_op = 1 + convert_ub(s1, s2, index1 + 1, index2 + 1)
    return min(delete_op, insert_op, replace_op)


print(convert_ub("table", "tbrlt"))
