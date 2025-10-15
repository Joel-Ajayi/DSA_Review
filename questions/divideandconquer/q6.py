"""
Longest Palindromic Subsequence

"""


def lps(S: str, start: int, end: int, memo: dict[tuple[int, int], str] = {}) -> str:
    if (start, end) in memo:
        return memo[(start, end)]

    if start == end:
        return S[start]
    if start > end:
        return ""

    # decisions
    if S[start] == S[end]:
        res = S[start] + lps(S, start + 1, end - 1, memo) + S[end]
    else:
        # Decisions
        # 1. Move to the next element from start
        # 2. move to the next element from end

        # where the current s1 value does not match
        push_end_sub_str = lps(S, start, end - 1, memo)
        push_start_sub_str = lps(S, start + 1, end, memo)
        res = max([push_end_sub_str, push_start_sub_str], key=lambda item: len(item))

    memo[(start, end)] = res
    return res


case = "ELRMENMET"
res = lps(case, 0, len(case) - 1)

print(res)
