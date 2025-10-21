#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity.
# If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days,
# they send the client a notification about potential fraud.
# The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

# Given the number of trailing days  and a client's total daily expenditures for a period of  days,
# determine the number of times the client will receive a notification over all  days.


def activityNotifications(expenditure, d):
    notification_count = 0
    counting_arr = [0] * 201
    for i, exp in enumerate(expenditure):
        # sort array with counting sort
        if i >= d:
            count_progress = 0
            median1 = -1
            median2 = -1

            target1 = d // 2  # even cases
            target2 = (d // 2) + 1  # odd cases

            is_even = d % 2 == 0

            for exp2 in range(201):
                count = counting_arr[exp2]
                count_progress += count

                if count_progress >= target1 and median1 == -1:
                    median1 = exp2

                if count_progress >= target2 and median2 == -1:
                    median2 = exp2

            # Slide the window: Remove the oldest day
            counting_arr[expenditure[i - d]] -= 1

            if is_even:
                median = sum([median1, median2]) / 2
            else:
                median = median2
            if exp >= (2 * median):
                notification_count += 1

        # increase frequency of current expenditure
        counting_arr[exp] += 1

    return notification_count
    # can check for notifications here
    # Write your code here
