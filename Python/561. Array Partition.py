# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ...,
# (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i, num in enumerate(nums, start=1):
            if i%2 != 0:
                result += num
        return result

nums = [1,4,3,2]
x = Solution()
print(x.arrayPairSum(nums))