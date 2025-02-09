# Given an array of integers arr, replace each element with its rank.
#
# The rank represents how large the element is. The rank has the following rules:
#
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

from typing import List
from collections import defaultdict

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        our_dict = defaultdict(int)
        i = 0
        for a in sorted(arr, reverse=False):
            if not a in our_dict:
                i += 1
                our_dict[a] = i

        result = [None] * len(arr)
        for index, a in enumerate(arr):
            result[index] = our_dict[a]

        return result

arr = [40,10,20,30]
x = Solution()
print(x.arrayRankTransform(arr))