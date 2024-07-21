# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# Find the maximum profit you can achieve. You may complete at most two transactions.
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

def maxProfit1(prices: list[int]) -> int:

    return profit


def maxProfit3(prices: list[int]) -> int: #чужой
    if not prices:
        return 0

    # initialize variables for first buy, first sell, second buy, and second sell
    buy1, buy2 = float('inf'), float('inf')
    profit1, profit2 = 0, 0

    # iterate over prices to update buy and sell values
    for price in prices:
        # update first buy and sell values
        buy1 = min(buy1, price)
        profit1 = max(profit1, price - buy1)
        # update second buy and sell values
        buy2 = min(buy2, price - profit1)
        profit2 = max(profit2, price - buy2)

    return profit2

def maxProfit4(prices: list[int]) -> int:
    OurFirstTrade, OurSecondTrade = max(prices), max(prices)
    OurFirstProfit, OurSecondProfit = 0, 0
    for value in prices:
        if value < OurFirstTrade:
            OurFirstTrade = value
        if (value - OurFirstTrade) > OurFirstProfit:
            OurFirstProfit = value - OurFirstTrade
        if (value - OurFirstProfit) < OurSecondTrade:
            OurSecondTrade = value - OurFirstProfit
        if (value - OurSecondTrade) > OurSecondProfit:
            OurSecondProfit = value - OurSecondTrade
    return OurSecondProfit

prices = [5,6,7,8,9,1,2,1,3]
profit = maxProfit4(prices)
print(profit)




