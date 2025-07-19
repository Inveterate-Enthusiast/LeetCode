# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.

from typing import List
from itertools import combinations

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int: # time limit exceeded
        combs = combinations(nums, 3)
        distance = float("inf")
        result = 0
        for i, j, k in combs:
            cur_sum = (i + j + k)
            if distance > (x := abs(target - cur_sum)):
                distance = x
                result = cur_sum

        return result

    def threeSumClosest1(self, nums: List[int], target: int) -> int:
        distance = float("inf")
        result = 0
        nums.sort()
        n = len(nums)
        for start in range(n - 2):
            left, right = (start + 1),  n - 1

            while left < right:
                cur_sum = nums[start] + nums[left] + nums[right]
                if cur_sum == target:
                    return target

                if distance > (x := abs(target - cur_sum)):
                    distance = x
                    result = cur_sum

                if cur_sum > target:
                    right -= 1
                else:
                    left += 1

        return result


nums = [-1,2,1,-4]
target = 1
x = Solution()
print(x.threeSumClosest1(nums, target))