def minimumBribes(q: list[int]):
    global_bribes = 0
    is_chaos = False

    # works but has issue with time complexity
    # for correct_id in range(len(q), 0, -1):
    #     local_bribes = 0
    #     moving_index = -1

    #     while q[correct_id - 1] != correct_id:
    #         moving_index = (
    #             q.index(correct_id) if moving_index == -1 else moving_index + 1
    #         )
    #         local_bribes += 1

    #         q[moving_index], q[moving_index + 1] = q[moving_index + 1], q[moving_index]

    #     global_bribes += local_bribes
    #     is_chaos = False if not is_chaos and local_bribes <= 2 else True

    for i in range(len(q), 0, -1):
        if q[i] != (i + 1):
            # If not, check if the correct person is one spot ahead.
            if (i - 1) >= 0 and q[i - 1] == (i + 1):
                # One bribe occurred.
                bribes += 1
                # Swap them to restore the person to their correct place for the next checks.
                q[i - 1], q[i] = q[i], q[i - 1]

            # Check if the correct person is two spots ahead.
            elif (i - 2) >= 0 and q[i - 2] == (i + 1):
                # Two bribes occurred.
                bribes += 2
                # "Bubble" the person back to their correct spot.
                q[i - 2], q[i - 1] = q[i - 1], q[i - 2]
                q[i - 1], q[i] = q[i], q[i - 1]

            # If the correct person is more than two spots away, it's chaotic.
            else:
                print("Too chaotic")
                return

    print(global_bribes)


minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
