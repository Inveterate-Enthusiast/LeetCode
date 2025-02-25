# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
#
# The value of |x| is defined as:
#
# x if x >= 0.
# -x if x < 0.

from typing import List
from collections import defaultdict

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        our_dict = defaultdict(int)
        result = 0
        for num in nums:
            if (x := (num - k)) in our_dict:
                result += our_dict[x]
            if (x := (num + k)) in our_dict:
                result += our_dict[x]
            our_dict[num] += 1
        return result

nums = [1,2,2,1]
k = 1
x = Solution()
print(x.countKDifference(nums, k))