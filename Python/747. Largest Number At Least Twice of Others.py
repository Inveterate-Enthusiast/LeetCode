# You are given an integer array nums where the largest integer is unique.
#
# Determine whether the largest element in the array is at least twice as much as every other number in the array.
# If it is, return the index of the largest element, or return -1 otherwise.
from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        l_first = l_second = 0
        result = -1
        for index, num in enumerate(nums):
            if not l_first:
                l_first = num; result = index
            elif not l_second:
                l_first, l_second = max(l_first, num), min(l_first, num)
                result = index if l_first == num else result
            else:
                if num > l_first:
                    l_second = l_first
                    l_first = num
                    result = index
                elif num > l_second:
                    l_second = num
        return result if l_first >= (2 * l_second) else (-1)

nums = [0,0,0,1]
x = Solution()
print(x.dominantIndex(nums))