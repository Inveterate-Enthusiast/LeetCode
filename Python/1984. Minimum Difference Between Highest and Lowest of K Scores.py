# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
#
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
#
# Return the minimum possible difference.

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        result = float("inf")
        nums_1 = sorted(nums)
        for i in range(k-1, len(nums_1)):
            result = min(result, (nums_1[i] - nums_1[i-k+1]))

        return result


nums = [64407,3036]
k = 2
x = Solution()
print(x.minimumDifference(nums, k))