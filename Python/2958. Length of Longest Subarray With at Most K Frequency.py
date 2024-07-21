# You are given an integer array nums and an integer k.
#
# The frequency of an element x is the number of times it occurs in an array.
#
# An array is called good if the frequency of each element in this array is less than or equal to k.
#
# Return the length of the longest good subarray of nums.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
from typing import List, Optional
from collections import deque, defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        _dict = defaultdict(int)
        left = 0; ansCount = 0
        for right in range(len(nums)):
            _dict[nums[right]] += 1
            while left <= right and _dict[nums[right]] > k:
                _dict[nums[left]] -= 1; left += 1

            if left <= right: ansCount = max(ansCount, (right - left + 1))

        return ansCount

nums = [1,2,3,1,2,3,1,2]; k = 2
X = Solution()
print(X.maxSubarrayLength(nums, k))






