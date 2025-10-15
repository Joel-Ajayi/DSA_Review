"""
Longest common sequence

"""


def lcq(
    s1: str,
    s2: str,
    memo: dict[tuple[str, str], str] = {},
) -> str:
    if (s1, s2) in memo:
        return memo[(s1, s2)]

    if not s1 or not s2:
        return ""

    # decisions
    if s1[-1] == s2[-1]:
        res = lcq(s1[:-1], s2[:-1], memo) + s1[-1]
    else:
        # where the current s1 value does not match
        s1_forwared_sub_str = lcq(s1[:-1], s2, memo)
        s2_forwared_sub_str = lcq(s1, s2[:-1], memo)

        options = [s1_forwared_sub_str, s2_forwared_sub_str]
        res = max(options, key=lambda item: len(item))

    memo[(s1, s2)] = res
    return res


res = lcq("elephant", "erepat")

print(res)
