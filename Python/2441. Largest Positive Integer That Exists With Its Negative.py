# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
#
# Return the positive integer k. If there is no such integer, return -1.

from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        our_set = set()
        result = (-1)
        for i in nums:
            if (-i) in our_set:
                result = max(result, abs(i))
            our_set.add(i)

        return result

nums = [-10,8,6,7,-2,-3]
x = Solution()
print(x.findMaxK(nums))