# Sherlock considers a string to be valid if all characters of the string appear the same number of times.
# It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times.
# Given a string , determine if it is valid. If so, return YES, otherwise return NO.


def isValid(s):
    # Write your code here
    char_freq = {}

    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    sorted_arr = sorted(char_freq.values())

    min_val = sorted_arr[0]
    max_val = sorted_arr[-1]

    if max_val > min_val and len(sorted_arr) >= 3:
        val_after_min = sorted_arr[1]
        val_before_max = sorted_arr[-2]

        if min_val == 1:
            if val_after_min != max_val:
                return "NO"
        else:
            if val_before_max > min_val or (max_val - val_before_max) > 1:
                return "NO"

    return "YES"


print(isValid("aaaabbcc"))
