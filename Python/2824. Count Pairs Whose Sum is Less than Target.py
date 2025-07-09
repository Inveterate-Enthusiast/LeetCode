# Given a 0-indexed integer array nums of length n and an integer target,
# return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

from typing import List
from itertools import combinations

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        combs = combinations(nums, 2)
        result = 0
        for i, j in combs:
            if (i + j) < target:
                result += 1

        return result

nums = [-1,1,2,3,1]
target = 2
x = Solution()
print(x.countPairs(nums, target))