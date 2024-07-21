# Given an integer array nums, handle multiple queries of the following type:
#
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements
# of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
from typing import Optional, List

class NumArray1:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1]) if left <= right else None

class NumArray2:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [0]*(len(self.nums)+1)
        for i in range(len(nums)):
            if i == 0:
                self.prefix_sum[i+1] = self.nums[i]
                continue
            self.prefix_sum[i+1] = self.prefix_sum[i] + self.nums[i]

    def sunRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left] if left <= right else None

X = NumArray2([-2,0,3,-5,2,-1])
print(X.sunRange(2, 5))