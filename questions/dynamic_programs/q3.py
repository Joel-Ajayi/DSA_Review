"""
You are given  queries. Each query is of the form two integers described below:
-  : Insert x in your data structure.
-  : Delete one occurence of y from your data structure, if present.
-  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element.

Return an array with the output. e.g [0,1]
"""


def freqQuery(queries: list[tuple[int, int]]):
    # sores items fequncy
    item_freq: dict[int, int] = {}
    # stores number of items with same frequency
    count_freq: dict[int, int] = {}

    return_arr = []

    for op, val in queries:
        if op == 1:
            item_freq[val] = 0
        if op == 3:
            count_freq[val] = 0

    for op, val in queries:
        if op == 1:
            prev_item_freq = item_freq[val]

            #  Check if value has been added before
            if prev_item_freq != 0:
                try:
                    # yes delete it from count freq is this count exist
                    freq = count_freq[prev_item_freq]
                    if freq != 0:
                        count_freq[prev_item_freq] -= 1
                except:
                    pass

            # Added to value to item and count history
            new_item_freq = prev_item_freq + 1
            item_freq[val] = new_item_freq
            try:
                count_freq[new_item_freq] += 1
            except:
                pass
        elif op == 2:
            prev_item_freq = item_freq.get(val, 0)

            if prev_item_freq != 0:
                new_item_freq = prev_item_freq - 1
                item_freq[val] = new_item_freq
                try:
                    freq = count_freq[prev_item_freq]
                    if freq != 0:
                        count_freq[prev_item_freq] -= 1
                except:
                    pass

                try:
                    count_freq[new_item_freq] += 1
                except:
                    pass

        else:
            if count_freq[val] != 0:
                return_arr.append(1)
            else:
                return_arr.append(0)

    return return_arr


print(freqQuery([(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]))
