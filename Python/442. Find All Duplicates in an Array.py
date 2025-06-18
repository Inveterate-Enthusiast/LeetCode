# Given an integer array nums of length n where all the integers of nums are in the range [1, n]
# and each integer appears at most twice, return an array of all the integers that appears twice.
#
# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = list()
        for num in nums:
            temp = abs(num) - 1
            if nums[temp] < 0:
                result.append(abs(num))
            else:
                nums[temp] = (-nums[temp])
        return result

nums = [10,2,5,10,9,1,1,4,3,7]
x = Solution()
print(x.findDuplicates(nums))