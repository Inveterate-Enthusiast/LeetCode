# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

from typing import List
from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        for num in nums:
            our_dict[num] += 1

        result = (-1)
        for num, freq in our_dict.items():
            if freq == 1:
                result = max(result, num)

        return result

nums = [5,7,3,9,4,9,8,3,1]
x = Solution()
print(x.largestUniqueNumber(nums))