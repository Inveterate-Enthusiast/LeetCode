# You are given a 0-indexed integer array nums and a target element target.
#
# A target index is an index i such that nums[i] == target.
#
# Return a list of the target indices of nums after sorting nums in non-decreasing order.
# If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = list()
        for index, num in enumerate(sorted(nums)):
            if num == target:
                result.append(index)

        return result

nums = [1,2,5,2,3]
target = 2
x = Solution()
print(x.targetIndices(nums, target))