"""
A taxi can take multiple passengers to the railway station at the same time.On the way back to the starting point,the taxi driver may pick up additional passengers for his next trip to the airport.A map of passenger location has been created,represented as a square matrix.

The Matrix is filled with cells,and each cell will have an initial value as follows:

A value greater than or equal to zero represents a path.
A value equal to 1 represents a passenger.
A value equal to -1 represents an obstruction.
The rules of motion of taxi are as follows:

The Taxi driver starts at (0,0) and the railway station is at (n-1,n-1).Movement towards the railway station is right or down,through valid path cells.
After reaching (n-1,n-1) the taxi driver travels back to (0,0) by travelling left or up through valid path cells.
When passing through a path cell containing a passenger,the passenger is picked up.once the rider is picked up the cell becomes an empty path cell.
If there is no valid path between (0,0) and (n-1,n-1),then no passenger can be picked.
The goal is to collect as many passengers as possible so that the driver can maximize his earnings.
For example consider the following grid,

           0      1
          -1     0

Start at top left corner.Move right one collecting a passenger. Move down one to the destination.Cell (1,0) is blocked,So the return path is the reverse of the path to the airport.All Paths have been explored and one passenger is collected.

Returns:

Int:maximum number of passengers that can be collected.
"""

# From each state (r1, c1, r2) there are 4 possible next moves:

# A goes down, B goes down

# A goes down, B goes right

# A goes right, B goes down

# A goes right, B goes right


def collectMax(paths: list[list[int]]):
    NEG = float("-inf")

    n, m = len(paths), len(paths[0])
    dp = [[NEG] * (n + 1) for _ in range(n + 1)]

    # Max number of steps:
    # tyically if you go down to last row and right to the last col
    # or right to the last col and down to the last row#
    max_steps = 2 * (n - 1)
    dp[1][1] = paths[0][0]

    for k in range(1, max_steps + 1):
        next_dp = [[NEG] * (n + 1) for _ in range(n + 1)]
        for r1 in range(1, n + 1):
            for r2 in range(1, n + 1):
                if dp[r1][r2] == NEG:
                    continue

                # Convert back to matrix coordinates
                c1 = k - (r1 - 1)
                c2 = k - (r2 - 1)

                if c1 < 1 or c1 >= (n + 1) or c2 < 0 or c2 >= n:
                    continue

                best_move = NEG
                # since both are assumed to have taken same number steps
                # Try all 4 moves:
                # (down,down), (down,right), (right,down), (right,right)
                # (r1+1, r2+1), (r1+1, r2), (r1, r2-1), (r1, r2)
                moves = [(r1 + 1, r2 + 1), (r1 + 1, r2), (r1, r2 + 1), (r1, r2)]
                # assigned to maximum number of apssengers picked

                for mr1, mr2 in moves:
                    best_move = max(best_move, dp[mr1][mr2])

                if best_move == NEG:
                    # unreachable state
                    continue

                if r1 == r2 and c1 == c2:
                    additiona_passeners = paths[r1][c1]
                else:
                    additiona_passeners = paths[r1][c1] + paths[r2][c2]

                passengers = best_move + additiona_passeners
                # add passengers at current positions (count once if same cell)
                next_dp[r1][r2] = max(passengers, next_dp[r1][r2])

        dp = next_dp

    print(dp)
    return dp[n][n]


print(collectMax([[0, 1, -1], [1, 0, -1], [1, 1, 1]]))
