# You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:
#
# 0 <= i < j < k < nums.length
# nums[i], nums[j], and nums[k] are pairwise distinct.
# In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
# Return the number of triplets that meet the conditions.

from typing import List
from itertools import combinations
from collections import defaultdict

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        combs = combinations(nums, 3)
        result = 0
        for i, j, k in combs:
            if i != j and i != k and j != k:
                result += 1

        return result

    def unequalTriplets1(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        for i in nums:
            our_dict[i] += 1

        nums_prev, nums_next = 0, len(nums)
        result = 0
        for key, nums_freq in our_dict.items():
            nums_next -= nums_freq
            result += nums_prev * nums_freq * nums_next
            nums_prev += nums_freq

        return result

nums = [4,4,2,4,3]
x = Solution()
print(x.unequalTriplets1(nums))