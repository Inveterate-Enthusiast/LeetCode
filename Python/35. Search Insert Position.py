# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
import math


class Solution:
    def searchInsert1(self, nums: list[int], target: int) -> int:
        low = 0; high = (len(nums)-1)
        while low <= high:
            mid = math.floor((high + low) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
        return high + 1


nums = [1,3,5,6]; target = 0
X = Solution()
print(X.searchInsert1(nums, target))