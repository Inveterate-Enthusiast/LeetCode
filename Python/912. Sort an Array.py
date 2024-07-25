# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
from typing import List, Optional

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]: # memory limit exeeded
        if len(nums) <= 1:
            return nums

        left, middle, right = list(), list(), list()
        bar = nums[0]
        for value in nums:
            if value == bar:
                middle.append(value)
            elif value < bar:
                left.append(value)
            else:
                right.append(value)
        left = self.sortArray(left)
        right = self.sortArray(right)
        return left + middle + right

    def merge(self, list1: List[int], list2: List[int]) -> List[int]: # additional function
        _list = [0] * ((x1 := len(list1)) + (x2 := len(list2)))
        i1 = i2 = 0
        for index in range(len(_list)):
            if i2 >= x2 or (i1 < x1 and list1[i1] <= list2[i2]):
                _list[index] = list1[i1]
                i1 += 1
            else:
                _list[index] = list2[i2]
                i2 += 1
        return _list
    def sortArray1(self, nums: List[int]) -> List[int]:
        if (x := (len(nums))) <= 1:
            return nums
        mid = x//2
        left = nums[:mid]
        right = nums[mid:]
        left, right = self.sortArray1(left), self.sortArray1(right)
        return self.merge(left, right)


X = Solution()
nums = [5,2,3,1]
print(X.sortArray(nums))