# You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.
#
# For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums.
# In other words, count the number of indices i such that:
#
# 0 <= i <= nums.length - 2,
# nums[i] == key and,
# nums[i + 1] == target.
# Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.

from typing import List
from collections import defaultdict

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        our_dict = defaultdict(int)
        prev_num = nums[0]
        our_max = 0
        result = None
        for i in range(1, len(nums)):
            if prev_num == key:
                our_dict[nums[i]] += 1
                if our_max < our_dict[nums[i]]:
                    result = nums[i]
                    our_max = our_dict[nums[i]]
            prev_num = nums[i]

        return result

nums = [1,100,200,1,100]
key = 1
x = Solution()
print(x.mostFrequent(nums, key))