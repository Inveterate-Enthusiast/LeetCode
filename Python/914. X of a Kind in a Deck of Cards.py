# You are given an integer array deck where deck[i] represents the number written on the ith card.
#
# Partition the cards into one or more groups such that:
#
# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise

from typing import List
from collections import defaultdict

class Solution:
    def help(self, a:int, b:int) -> int:
        big = a if a >= b else b
        small = b if b <= a else a
        while big != 0 and small != 0:
            big, small = small, (big % small)
        return (big + small)

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        our_dict = defaultdict(int)
        for i in deck:
            our_dict[i] += 1

        our_list = list(our_dict.values())
        temp = our_list[0]
        for i in range(1, len(our_list)):
            if (temp:=(self.help(our_list[i], temp))) <= 1:
                return False
        return temp != 1

deck = [1]
x = Solution()
print(x.hasGroupsSizeX(deck))