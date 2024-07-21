# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

def maxProfit1(prices: list[int]) -> int:
    start = 0
    profit = 0
    for i, value in enumerate(prices):
        if i == 0:
            minValue = value
            maxValue = value
        else:
            if value < minValue:
                minValue = value
                start = i
            elif value > maxValue and start <= i:
                maxValue = value
                profit = max(profit, (maxValue - minValue))
    return profit


def maxProfit2(prices: list[int]) -> int:
    minValue = prices[0]
    profit = 0
    for i, value in enumerate(prices):
        if value < minValue:
            minValue = value
        elif (value - minValue) > profit:
            profit = value - minValue
    return profit

def maxProfit3(prices: list[int]) -> int:
    if not prices:
        return 0
    OurMaxProfit = 0
    OurMinPrice = prices[0]
    for price in prices[1:]:
        OurMinPrice = min(OurMinPrice, price)
        OurMaxProfit = max(OurMaxProfit, price - OurMinPrice)
    return OurMaxProfit

prices1 = [7,6,5,6,7,8]
prices2 = [7,1,5,3,6,4]
profit = maxProfit3(prices2)
print(profit)