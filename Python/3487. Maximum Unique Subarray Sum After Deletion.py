# You are given an integer array nums.
#
# You are allowed to delete any number of elements from nums without making it empty.
# After performing the deletions, select a subarray of nums such that:
#
# All elements in the subarray are unique.
# The sum of the elements in the subarray is maximized.
# Return the maximum sum of such a subarray.

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        set_pos, set_neg = set(), set()
        sum_pos, sum_neg = 0, float("-inf")
        for i in nums:
            if (i >= 0) and (i not in set_pos):
                sum_pos += i
                set_pos.add(i)
            if i < 0 and (i not in set_neg):
                sum_neg = max(sum_neg, i)
                set_neg.add(i)
        return sum_pos if len(set_pos) > 0 else sum_neg

nums = [-100]
x = Solution()
print(x.maxSum(nums))