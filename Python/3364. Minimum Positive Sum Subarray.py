# You are given an integer array nums and two integers l and r.
# Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive)
# and whose sum is greater than 0.
#
# Return the minimum sum of such a subarray. If no such subarray exists, return -1.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        result = float("inf")

        for our_len in range(l, r + 1):
            temp_sum, left = 0, 0
            for right in range(n):
                temp_sum += nums[right]
                while (right - left + 1) > our_len:
                    temp_sum -= nums[left]
                    left += 1
                if (right - left + 1) == our_len and temp_sum > 0:
                    result = min(result, temp_sum)
        return result if result != float("inf") else (-1)

nums = [3, -2, 1, 4]
l = 2
r = 3
x = Solution()
print(x.minimumSumSubarray(nums, l, r))