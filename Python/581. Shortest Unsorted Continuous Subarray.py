# Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.
#
# Return the shortest such subarray and output its length.
from typing import List, Optional
from collections import defaultdict, deque

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left, right = len(nums), 0
        OurStack = deque()
        for index, value in enumerate(nums):
            while OurStack and nums[OurStack[-1]] > value:
                left = min(left, OurStack.pop())
            OurStack.append(index)

        OurStack = deque()
        for index in range(len(nums)-1, -1, -1):
            while OurStack and nums[OurStack[-1]] < nums[index]:
                right = max(right, OurStack.pop())
            OurStack.append(index)

        return (right - left + 1) if left < right else 0




X = Solution()
nums = [2,6,4,8,10,9,15]
print(X.findUnsortedSubarray(nums))