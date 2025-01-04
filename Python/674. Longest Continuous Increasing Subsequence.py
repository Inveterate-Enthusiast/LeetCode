# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray).
# The subsequence must be strictly increasing.
#
# A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ...,
# nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left = right = 0
        result = 0
        while left <= right and right < len(nums):
            if left == right or nums[right - 1] < nums[right]:
                result = max(result, (right - left + 1))
                right += 1
            else:
                left = right
        return result

nums = [1, 2]
x = Solution()
print(x.findLengthOfLCIS(nums))