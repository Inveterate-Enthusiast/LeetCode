# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

from typing import List, Optional

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)

    def removeElement1(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left

nums = [0,1,2,2,3,0,4,2]; val = 2
X = Solution()
print(X.removeElement(nums, val))
print(nums)
