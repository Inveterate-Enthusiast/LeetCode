# You are given a non-negative integer array nums. In one operation, you must:
#
# Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
# Subtract x from every positive element in nums.
# Return the minimum number of operations to make every element in nums equal to 0.

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        temp_min = float("inf")
        for i in nums:
            if i > 0:
                temp_min = min(temp_min, i)
        cur_min = temp_min if temp_min != float("inf") else 0
        result = 0
        while cur_min != 0:
            temp_min = 0
            for idx, value in enumerate(nums):
                if value > 0:
                    nums[idx] = value - cur_min
                    if nums[idx] > 0:
                        temp_min = nums[idx] if temp_min == 0 else min(temp_min, nums[idx])
            result += 1
            cur_min = temp_min

        return result

    def minimumOperations1(self, nums: List[int]) -> int:
        result = len(set(nums) - {0})
        return result

nums = [1,5,0,3,5]
x = Solution()
print(x.minimumOperations1(nums))