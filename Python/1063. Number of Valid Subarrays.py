# Given an integer array nums, return the number of non-empty subarrays
# with the leftmost element of the subarray not larger than other elements in the subarray.
#
# A subarray is a contiguous part of an array.
from typing import List
from collections import deque
class Solution:
    def validSubarrays1(self, nums: List[int]) -> int:
        ansCount = 0

        for i in range(len(nums)):
            temp_ans = 1
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    break
                temp_ans += 1
            ansCount += temp_ans
        return ansCount

    def validSubarrays2(self, nums: List[int]) -> int:
        ansCount = 0
        OurStack = deque()
        _len = len(nums)

        for i in range(_len):
            while OurStack and nums[OurStack[-1]] > nums[i]:
                OurStack.pop()
            OurStack.append(i)
            ansCount += len(OurStack)
        return ansCount

    def validSubarrays3(self, nums: List[int]) -> int:
        _len = len(nums)
        OurStack = list()
        ansCount = 0
        nextSmallest = [_len] * _len

        for i in range(_len):
            while OurStack and nums[OurStack[-1]] > nums[i]:
                nextSmallest[OurStack.pop()] = i
            OurStack.append(i)

        for i in range(_len):
            ansCount += (nextSmallest[i] - i)

        return ansCount


nums = [2,2,2]
X = Solution()
print(X.validSubarrays2(nums))

