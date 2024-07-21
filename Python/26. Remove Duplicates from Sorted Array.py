# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements
# in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
from typing import List, Optional
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curInt = nums[0]; i = 1
        genLen = len(nums); ansCount = 0
        while i < len(nums):
            if curInt == nums[i]:
                del nums[i]
                ansCount += 1
            else:
                curInt = nums[i]; i += 1

        return genLen - ansCount

nums = [1,1,2]
X = Solution()
print(X.removeDuplicates1(nums))