# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])

nums = [-4,-1,0,3,10]
x = Solution()
print(x.sortedSquares(nums))