"""
Coin chain problem
"""

denominations = [1, 2, 5, 10, 20, 50, 100, 1000]
total_amt = 2035


def getMinNumCoins():
    sorted_denominations = sorted(denominations, reverse=True)
    remaining = total_amt
    count = 0
    i = 0

    while i < len(sorted_denominations) and remaining > 0:
        current_coin_val = sorted_denominations[i]
        if remaining >= current_coin_val:
            remaining -= current_coin_val
            count += 1

            if remaining < current_coin_val:
                i += 1
        else:
            i += 1
    return count if remaining == 0 else 0


print(getMinNumCoins())
