# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
from operator import index
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for idx in range(n):
            i = idx
            for j in range((i + 1), n):
                if nums[j] < nums[i]:
                    i = j
            nums[idx], nums[i] = nums[i], nums[idx]

    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j + 1] < nums[j]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]

    def sortColors3(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        left, middle, right = list(), list(), list()
        barrier = nums[0]
        for num in nums:
            if num == barrier:
                middle.append(num)
            elif num < barrier:
                left.append(num)
            else:
                right.append(num)

        self.sortColors3(left)
        self.sortColors3(right)
        i = 0
        for num in (left + middle + right):
            nums[i] = num; i += 1



nums = [2,0,2,1,1,0]
x = Solution()
x.sortColors3(nums)
print(nums)