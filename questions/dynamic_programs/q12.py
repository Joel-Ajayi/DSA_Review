"""
For strings s1 and s2
Fine the longest common subsequence
"""


def subsequence(
    s1: str,
    s2: str,
):
    len1, len2 = len(s1), len(s2)
    dp = [0] * (len2 + 1)

    # row - s1
    # col - s2
    for i in range(len1):
        new_dp = [0] * (len2 + 1)
        for j in range(1, len2 + 1):
            # when characters match
            if s1[i] == s2[j - 1]:
                new_dp[j] = 1 + dp[j - 1]
                continue

            skip_s1 = dp[j]
            skip_s2 = new_dp[j - 1]
            new_dp[j] = max(skip_s1, skip_s2)

        dp = new_dp

    return dp[-1]


print(subsequence("ADCB", "ABC"))
