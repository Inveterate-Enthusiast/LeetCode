# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
#
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
#
# 0 <= i, j < nums.length
# i != j
# |nums[i] - nums[j]| == k
# Notice that |val| denotes the absolute value of val.

from typing import List
from itertools import combinations
from collections import defaultdict

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        our_combs = combinations(nums, 2)
        our_diffs = set()
        for i, j in our_combs:
            if abs(i - j) == k:
                our_diffs.add((i if i <= j else j, j if i <= j else i))
        return len(our_diffs)

    def findPairs1(self, nums: List[int], k: int) -> int:
        our_dict = defaultdict(int)
        for i in nums:
            our_dict[i] += 1
        result = 0
        if k == 0:
            for i in our_dict.values():
                if i > 1: result += 1
        else:
            for i in our_dict.keys():
                if (i - k) in our_dict:
                    result += 1

        return result

nums = [1,3,1,5,4]
k = 0
x = Solution()
print(x.findPairs1(nums, k))