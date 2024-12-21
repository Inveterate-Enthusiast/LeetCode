# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor



X = Solution()
nums1 = [2, 2, 1]
print(X.singleNumber(nums1))

nums2 = [4, 1, 2, 1, 2]
print(X.singleNumber(nums2))