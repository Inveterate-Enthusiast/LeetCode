# Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
#
# nums[a] + nums[b] + nums[c] == nums[d], and
# a < b < c < d

from typing import List
from itertools import combinations

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        our_combs = combinations(nums, 4)
        result = 0
        for a, b, c, d in our_combs:
            if (a + b + c) == d:
                result += 1
        return result

nums = [1,1,1,3,5]
x = Solution()
print(x.countQuadruplets(nums))