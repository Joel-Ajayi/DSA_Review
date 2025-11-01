def myLoss(prices: list[int]):
    max_loss = 0

    for i in range(len(prices) - 1):
        for j in range(i, len(prices)):
            loss = prices[i] - prices[j]
            max_loss = max(max_loss, loss)

    return max_loss


print(myLoss([1, 2, 3, 4]))
