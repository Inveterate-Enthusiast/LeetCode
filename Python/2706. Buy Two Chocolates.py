# You are given an integer array prices representing the prices of various chocolates in a store.
# You are also given a single integer money, which represents your initial amount of money.
#
# You must buy exactly two chocolates in such a way that you still have some non-negative leftover money.
# You would like to minimize the sum of the prices of the two chocolates you buy.
#
# Return the amount of money you will have leftover after buying the two chocolates.
# If there is no way for you to buy two chocolates without ending up in debt, return money.
# Note that the leftover must be non-negative.

from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        x1, x2 = float("inf"), float("inf")
        for x in prices:
            if x < x1:
                x2, x1 = x1, x
            elif x < x2:
                x2 = x

        return (money - (x1 + x2)) if (x1 + x2) <= money else money

prices = [1,2,2]
money = 3
x = Solution()
print(x.buyChoco(prices, money))