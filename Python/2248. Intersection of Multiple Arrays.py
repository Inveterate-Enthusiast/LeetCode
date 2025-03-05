# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers,
# return the list of integers that are present in each array of nums sorted in ascending order.

from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        our_set = set(nums[0])
        for i in range(1, len(nums)):
            cur_set = set(nums[i])
            our_set = our_set.intersection(cur_set)
        return sorted(list(our_set))


nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
x = Solution()
print(x.intersection(nums))