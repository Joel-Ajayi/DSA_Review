# Number of paths in a matrix


def dp(rows: int, cols: int):
    prev_row = [0] * (cols + 1)

    for r in range(1, rows + 1):
        curr_row = [0] * (cols + 1)

        for c in range(1, cols + 1):
            if c == 1 and r == 1:
                curr_row[c] = 1
                continue

            curr_row[c] = curr_row[c - 1] + prev_row[c]
        prev_row = curr_row

    return prev_row[-1]


print(dp(4, 4))
