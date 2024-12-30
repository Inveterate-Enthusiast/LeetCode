# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        nums.sort()
        for i in range(result):
            if i == 0 and nums[i] != 0:
                result = 0
            elif i > 0 and (nums[i] - nums[i-1]) != 1:
                result = nums[i] - 1
        return result

    def missingNumber1(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result = result ^ i
        for i in range(len(nums)):
            result = result ^ i
        return result ^ (i + 1)

nums = [3, 0, 1]
x = Solution()
print(x.missingNumber1(nums))