# Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum.
# Note that the two subarrays must begin at different indices.
#
# Return true if these subarrays exist, and false otherwise.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        our_set = set()
        for i in range(1,len(nums)):
            x = nums[i] + nums[i-1]
            if x in our_set:
                return True
            our_set.add(x)

        return False

nums = [77,95,90,98,8,100,88,96,6,40,86,56,98,96,40,52,30,33,97,72,54,15,33,77,78,8,21,47,99,48]
x = Solution()
print(x.findSubarrays(nums))