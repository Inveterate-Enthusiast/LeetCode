# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

def maxProfit1(prices: list[int]) -> int: #расчет чисто для лонгов и шортов
    minValue, maxValue = prices[0], prices[0]
    profit = 0
    for i, value in enumerate(prices):
        if value < minValue:
            minValue = value
        elif value > maxValue:
            maxValue = value
        profit = max(profit, (maxValue - minValue), (minValue - maxValue))
    return profit

def maxProfit2(prices: list[int]) -> int:
    minValue, maxValue = prices[0], prices[0]
    profit, currentSum = 0, 0
    for i, value in enumerate(prices):
        if value < minValue or value < maxValue:
            profit += currentSum
            currentSum = 0
            minValue = value
            maxValue = value
        elif (value - minValue) > currentSum:
            currentSum = value - minValue
            maxValue = value
    else:
        profit += currentSum
    return profit

def maxProfit3(prices: list[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += (prices[i] - prices[i-1])
    return profit

prices = [1,2,3,4,5]
profit = maxProfit3(prices)
print(profit)