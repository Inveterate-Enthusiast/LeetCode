# You are given an integer array nums consisting of 2 * n integers.
#
# You need to divide nums into n pairs such that:
#
# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.

from typing import List
from collections import defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        l = len(nums)
        if (l % 2) != 0:
            return False

        our_dict = defaultdict(int)
        for num in nums:
            our_dict[num] += 1

        for k, v in our_dict.items():
            if v%2 != 0:
                return False

        return True

nums = [3,2,3,2,2,2]
x = Solution()
print(x.divideArray(nums))