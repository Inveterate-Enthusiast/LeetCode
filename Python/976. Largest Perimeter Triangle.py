# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
# formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        temp = sorted(nums, reverse=True)
        for i in range(2, len(temp)):
            if temp[i - 2] < (temp[i - 1] + temp[i]):
                return sum(temp[i-2:i+1])
        return 0

nums = [1,2,1,10]
x = Solution()
print(x.largestPerimeter(nums))