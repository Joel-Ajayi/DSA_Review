def max_passengers(matrix):
    n = len(matrix)
    NEG_INF = float("-inf")
    max_steps = 2 * (n - 1)

    # dp[k][r1][r2]: max passengers after k steps, path1 at (r1, c1), path2 at (r2, c2)
    dp = [[[NEG_INF] * (n + 1) for _ in range(n + 1)] for _ in range(max_steps + 1)]
    dp[0][1][1] = matrix[0][0]

    for k in range(max_steps):
        for r1 in range(1, n + 1):
            for r2 in range(1, n + 1):
                c1 = k + 2 - r1  # since r1 + c1 = k + 2
                c2 = k + 2 - r2
                if c1 < 1 or c1 > n or c2 < 1 or c2 > n:
                    continue
                if dp[k][r1][r2] == NEG_INF:
                    continue
                # Try all 4 move combinations
                for dr1, dc1 in [(1, 0), (0, 1)]:
                    for dr2, dc2 in [(1, 0), (0, 1)]:
                        nr1, nc1 = r1 + dr1, c1 + dc1
                        nr2, nc2 = r2 + dr2, c2 + dc2
                        if nr1 > n or nc1 > n or nr2 > n or nc2 > n:
                            continue
                        if (
                            matrix[nr1 - 1][nc1 - 1] == -1
                            or matrix[nr2 - 1][nc2 - 1] == -1
                        ):
                            continue
                        val = dp[k][r1][r2]
                        val += matrix[nr1 - 1][nc1 - 1]
                        if nr1 != nr2 or nc1 != nc2:
                            val += matrix[nr2 - 1][nc2 - 1]
                        dp[k + 1][nr1][nr2] = max(dp[k + 1][nr1][nr2], val)
    result = dp[max_steps][n][n]
    return max(0, result) if result != NEG_INF else 0


# Test cases
print(max_passengers([[0, 1], [-1, 0]]))  # Expected: 1
print(
    max_passengers([[0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
)  # Expected: 2
print(max_passengers([[0, 1, -1], [1, 0, -1], [1, 1, 1]]))  # Expected: 5
