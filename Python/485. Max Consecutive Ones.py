# Given a binary array nums, return the maximum number of consecutive 1's in the array.
from typing import List, Optional

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = 0
        left = 0
        for right, value in enumerate(nums):
            if not value:
                left = right+1
            else:
                maxLength = max(maxLength, (right - left + 1))
        return maxLength

