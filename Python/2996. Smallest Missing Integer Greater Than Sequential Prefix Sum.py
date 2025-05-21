# You are given a 0-indexed array of integers nums.
#
# A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.
#
# Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq_sum = nums[0]
        our_set = set(nums)

        for i in range(1, len(nums)):
            if nums[i] != (nums[i-1] + 1):
                break
            seq_sum += nums[i]

        i = 0
        while (seq_sum + i) in our_set:
            i += 1

        return seq_sum + i


nums = [3,4,5,1,12,14,13]
x = Solution()
print(x.missingInteger(nums))