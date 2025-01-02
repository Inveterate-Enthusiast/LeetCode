# You have a set of integers s, which originally contains all the numbers from 1 to n.
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
# which results in repetition of one number and loss of another number.
#
# You are given an integer array nums representing the data status of this set after the error.
#
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        our_max = len(nums)
        our_list = [i for i in range(1, our_max + 1, 1)]
        result = [None, None]
        i = j = 0
        while i < len(our_list) and j < len(nums):
            if our_list[i] < nums[j]:
                result[1] = our_list[i]
                i += 1
            elif our_list[i] > nums[j]:
                result[0] = nums[j]
                j += 1
            else:
                i += 1; j += 1
        else:
            if i < len(our_list): result[1] = our_list[i]
            if j < len(nums): result[0] = nums[j]
        return result

nums = [1,2,3,3]
x = Solution()
print(x.findErrorNums(nums))