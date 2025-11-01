def min_encyclopedias(shelf, k):
    """
    Optimized greedy algorithm using caching.
    Time Complexity: O(k * n * m)
    Space Complexity: O(k * (n + m))
    """
    if not shelf or not shelf[0]:
        return 0

    n, m = len(shelf), len(shelf[0])

    # Cache: count of each author in each row and column
    row_count: dict[tuple[int, int], int] = {}
    col_count: dict[tuple[int, int], int] = {}

    # Initialize counts
    for i in range(n):
        for j in range(m):
            author = shelf[i][j]
            if author > 0:
                row_count[(i, author)] = row_count.get((i, author), 0) + 1
                col_count[(j, author)] = col_count.get((j, author), 0) + 1

    selections = 0
    time_count = n
    # Continue until all counts are zero
    while row_count or col_count:
        time_count += 1
        best_i, best_j, best_author = -1, -1, -1
        max_removed = 0

        for i, author_i in row_count:
            for j, author_j in col_count:
                if author_i == author_j:
                    author = author_j
                    removed = row_count[(i, author)] + col_count[(j, author)] - 1
                    if removed > max_removed:
                        max_removed = removed
                        best_i, best_j, best_author = i, j, author

        if max_removed <= 0:  # No more books
            break

        # Remove all books with this author in this row and column
        del row_count[(best_i, best_author)]
        del col_count[(best_j, best_author)]

        for i in range(n):
            if (i, best_author) in row_count:
                count = row_count[(i, best_author)]
                if count == 1:
                    del row_count[(i, best_author)]
                else:
                    row_count[(i, best_author)] -= 1

        for j in range(m):
            if (j, best_author) in col_count:
                count = col_count[(j, best_author)]
                if count == 1:
                    del col_count[(j, best_author)]
                else:
                    col_count[(j, best_author)] -= 1

        selections += 1
    print(time_count)
    return selections


shelf = [[2, 2, 1], [1, 1, 1], [2, 3, 3]]
num_authors = 3

print(min_encyclopedias(shelf, num_authors))


# from collections import defaultdict

# # --- Union-Find Helper Functions ---
# # These operate on a shared 'parent' dictionary and 'num_components' count.
# parent = {}
# num_components = 0


# def find_set(item_id):
#     """Finds the representative (root) of the set containing item_id."""
#     # If item_id is its own parent, it's the root
#     if parent[item_id] == item_id:
#         return item_id
#     # Path compression: Make node point directly to the root
#     parent[item_id] = find_set(parent[item_id])
#     return parent[item_id]


# def unite_sets(item_id_a, item_id_b):
#     """Merges the sets containing item_id_a and item_id_b."""
#     global num_components
#     root_a = find_set(item_id_a)
#     root_b = find_set(item_id_b)
#     # If they are already in the same set, do nothing
#     if root_a != root_b:
#         # Merge the sets by making one root parent of the other
#         parent[root_b] = root_a
#         # Decrement the count of distinct components
#         num_components -= 1
#         return True
#     return False


# # ------------------------------------


# def organizeEncyclopedias(grid, k):
#     """
#     Calculates the minimum number of selections using Union-Find.
#     """
#     global parent, num_components  # Use the global UF variables
#     parent = {}

#     rows = len(grid)
#     cols = len(grid[0])
#     num_components = rows * cols

#     # Dictionary to store locations for each author
#     # author_id -> list of (row, col) tuples
#     author_locations = defaultdict(list)

#     # 1. Initialize Union-Find structure for each encyclopedia
#     for r in range(rows):
#         for c in range(cols):
#             author = grid[r][c]
#             # Use the tuple (r, c) as the unique ID for each item
#             loc_id = (r, c)
#             parent[loc_id] = loc_id  # Each item is initially its own parent
#             author_locations[author].append(loc_id)

#     # 2. Perform unions based on rows and columns for each author
#     for author in author_locations.keys():
#         locations = author_locations[author]

#         # Use dictionaries to quickly group locations by row/column
#         rows_map = defaultdict(list)
#         cols_map = defaultdict(list)
#         for r, c in locations:
#             rows_map[r].append((r, c))
#             cols_map[c].append((r, c))

#         # Union all encyclopedias by the same author in the same row
#         for r in rows_map:
#             if len(rows_map[r]) > 1:
#                 first_item_in_row = rows_map[r][0]
#                 for i in range(1, len(rows_map[r])):
#                     unite_sets(first_item_in_row, rows_map[r][i])

#         # Union all encyclopedias by the same author in the same column
#         for c in cols_map:
#             if len(cols_map[c]) > 1:
#                 first_item_in_col = cols_map[c][0]
#                 for i in range(1, len(cols_map[c])):
#                     unite_sets(first_item_in_col, cols_map[c][i])

#     # 3. The final count of components is the answer
#     return num_components


# # --- Example Usage ---
# shelf = [[2, 2, 1], [1, 1, 1], [2, 3, 3]]
# num_authors = 3
# print(
#     f"Minimum selections needed: {organizeEncyclopedias(shelf, num_authors)}"
# )  # Output: 3
