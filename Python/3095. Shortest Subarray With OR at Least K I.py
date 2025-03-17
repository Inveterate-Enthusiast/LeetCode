# You are given an array nums of non-negative integers and an integer k.
#
# An array is called special if the bitwise OR of all of its elements is at least k.
#
# Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

from typing import List
from functools import reduce

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = float("inf")
        for i in range(n):
            for j in range(i, n):
                x = reduce(lambda acc, x: acc | x, nums[i:j+1], 0) >= k
                if x: result = min(result, j - i + 1)
        return result if not result == float("inf") else (-1)

    def minimumSubarrayLength1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = float("inf")
        for i in range(n):
            temp = 0
            for j in range(i, n):
                temp |= nums[j]
                if (temp >= k): result = min(result, j - i + 1)
        return result if not result == float("inf") else (-1)

nums = [1,2,3]
k = 2
x = Solution()
print(x.minimumSubarrayLength1(nums, k))