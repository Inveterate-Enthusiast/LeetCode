# Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater
# element appear in nums.

from typing import List
from collections import defaultdict

class Solution:
    def countElements(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        our_min, our_max = float("inf"), float("-inf")

        for num in nums:
            our_dict[num] += 1
            if num > our_max: our_max = num
            if num < our_min: our_min = num

        result = 0
        for num, freq in our_dict.items():
            if num != our_min and num != our_max:
                result += freq

        return result

nums = [-71,-71,93,-71,40]
x = Solution()
print(x.countElements(nums))