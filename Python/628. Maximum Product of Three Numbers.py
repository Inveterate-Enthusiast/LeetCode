# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
from typing import List
from functools import reduce

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        ans1 = nums[0] * nums[1] * nums[-1]
        ans2 = reduce(lambda acc, x: acc * x, nums[-1:-3-1:-1], 1)
        return max(ans1, ans2)

nums = [-100,-98,-1,2,3,4]
x = Solution()
print(x.maximumProduct(nums))