#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def recusriveFinder(
    memo: dict[str, int] = {},
):
    s = "cdcd"
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            search_s = "".join(sorted(s[i:j]))
            memo[search_s] = memo.get(search_s, 0) + 1

    total_pairs = 0
    print(memo)
    for count in memo.values():
        if count != 1:
            print(count)
            total_pairs += count * (count - 1) // 2
    return total_pairs


print(recusriveFinder())
