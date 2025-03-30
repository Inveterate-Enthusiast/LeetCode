# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

from typing import List
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        our_dict = defaultdict(list)
        for i in range(len(nums)):
            our_dict[nums[i]].append(i)

        result = 0
        for key, value in our_dict.items():
            n = len(value)
            if n > 1:
                result += ((n * (n-1)) // 2)

        return result

    def numIdenticalPairs1(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        for i in range(len(nums)):
            our_dict[nums[i]] += 1

        result = 0
        for key, value in our_dict.items():
            if value > 1:
                result += ((value * (value - 1)) // 2)

        return result


nums = [1,2,3,1,1,3]
x = Solution()
print(x.numIdenticalPairs1(nums))