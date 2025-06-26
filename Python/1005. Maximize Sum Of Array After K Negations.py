# Given an integer array nums and an integer k, modify the array in the following way:
#
# choose an index i and replace nums[i] with -nums[i].
# You should apply this process exactly k times. You may choose the same index i multiple times.
#
# Return the largest possible sum of the array after modifying it in this way.

from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums_sort = sorted(nums)
        if nums_sort[0] >= 0 and (k % 2) == 0:
            return sum(nums)

        i = 0
        while i < len(nums_sort) and nums_sort[i] < 0 and k > 0:
            nums_sort[i] = (nums_sort[i] * (-1))
            i += 1
            k -= 1

        if (k == 0) or (k > 0 and (k % 2) == 0):
            return sum(nums_sort)
        else:
            nums_sort = sorted(nums_sort)
            nums_sort[0] = (nums_sort[0] * (-1))
            return sum(nums_sort)

nums = [2,-3,-1,5,-4]
k = 2
x = Solution()
print(x.largestSumAfterKNegations(nums, k))