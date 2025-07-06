# You have a water dispenser that can dispense cold, warm, and hot water.
# Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.
#
# You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2]
# denote the number of cold, warm, and hot water cups you need to fill respectively.
# Return the minimum number of seconds needed to fill up all the cups.

from typing import List
from math import ceil

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), ceil(sum(amount) / 2))

    def fillCups1(self, amount: List[int]) -> int:
        result = 0
        amount.sort(reverse=True)
        while amount[0] and amount[1]:
            amount[0] -= 1
            amount[1] -= 1
            amount.sort(reverse=True)
            result += 1
        result += amount[0]
        return result

amount = [1,4,2]
x = Solution()
print(x.fillCups1(amount))