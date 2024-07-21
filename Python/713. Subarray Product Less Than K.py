# Given an array of integers nums and an integer k,
# return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
from typing import List, Optional
from collections import deque

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        left = 0; ansCount = 0; curProduct = 1
        for right in range(len(nums)):
            curProduct *= nums[right]
            while left <= right and curProduct >= k:
                curProduct /= nums[left]; left += 1

            if curProduct < k: ansCount += (right - left + 1)

        return ansCount


nums = [10,5,2,6]; k = 100
X = Solution()
print(X.numSubarrayProductLessThanK(nums, k))
