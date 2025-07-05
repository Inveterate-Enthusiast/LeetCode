# Given an integer array nums containing distinct positive integers,
# find and return any number from the array that is neither the minimum nor the maximum value in the array,
# or -1 if there is no such number.
#
# Return the selected integer.

from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return (-1)

        x1, x2 = nums[0], nums[-1]
        for num in nums:
            if num < x1:
                x1 = num
            elif num > x2:
                x2 = num

        for num in nums:
            if x1 < num < x2:
                return num

        return (-1)

nums = [3,2,1,4]
x = Solution()
print(x.findNonMinOrMax(nums))