# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
#
# Return any such subsequence as an integer array of length k.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)], key=lambda x: x[0])
        return [num[0] for num in sorted(sorted_nums[-1 - k + 1:], key=lambda x: x[1])]


nums = [-1,-2,3,4]
k = 3
x = Solution()
print(x.maxSubsequence(nums, k))