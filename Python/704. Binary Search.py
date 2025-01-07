# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        our_len = len(nums)
        left, right = 0, (our_len - 1)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

nums = [9]; target = 9
x = Solution()
print(x.search(nums, target))