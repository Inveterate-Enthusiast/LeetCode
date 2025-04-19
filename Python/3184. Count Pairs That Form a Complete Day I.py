# Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j
# where i < j and hours[i] + hours[j] forms a complete day.
#
# A complete day is defined as a time duration that is an exact multiple of 24 hours.
#
# For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

from typing import List
from itertools import combinations
from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        combs = combinations(hours, 2)
        result = 0
        for i, j in combs:
            if ((i + j) % 24) == 0:
                result += 1

        return result

    def countCompleteDayPairs1(self, hours: List[int]) -> int:
        our_dict = defaultdict(int)
        result = 0
        for i in hours:
            j = (24 - (i % 24)) % 24
            if j in our_dict:
                result += our_dict[j]
            our_dict[(i % 24)] += 1

        return result

hours = [12,12,30,24,24]
x = Solution()
print(x.countCompleteDayPairs1(hours))