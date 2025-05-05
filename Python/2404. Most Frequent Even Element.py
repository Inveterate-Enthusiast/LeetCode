# Given an integer array nums, return the most frequent even element.
#
# If there is a tie, return the smallest one. If there is no such element, return -1.

from typing import List
from collections import defaultdict

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        our_max = 0
        for i in nums:
            if (i % 2) == 0:
                our_dict[i] += 1
                our_max = max(our_max, our_dict[i])

        result = float("inf")
        for num, freq in our_dict.items():
            if freq == our_max:
                result = min(result, num)

        return result if not result == float("inf") else (-1)

nums = [0,1,2,2,4,4,1]
x = Solution()
print(x.mostFrequentEven(nums))