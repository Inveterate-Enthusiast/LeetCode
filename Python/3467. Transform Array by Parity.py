# You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:
#
# Replace each even number with 0.
# Replace each odd numbers with 1.
# Sort the modified array in non-decreasing order.
# Return the resulting array after performing these operations.

from typing import List
from functools import reduce

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted([1 if ((i % 2) != 0) else 0 for i in nums])

    def transformArray1(self, nums: List[int]) -> List[int]:
        even_cnt = reduce(lambda acc, x: (acc + 1) if ((x % 2) == 0) else acc, nums, 0)
        return ([0] * even_cnt) + ([1] * (len(nums) - even_cnt))

nums = [4,3,2,1]
x = Solution()
print(x.transformArray1(nums))