# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mask = set([i for i in range(1, len(nums) + 1)])
        return list(mask.difference(set(nums)))



nums = [1, 1]
x = Solution()
print(x.findDisappearedNumbers(nums))