# You are given a 0-indexed array nums of length n.
#
# The distinct difference array of nums is an array diff of length n such that diff[i] is equal to the number of distinct
# elements in the suffix nums[i + 1, ..., n - 1] subtracted from the number of distinct elements in the prefix nums[0, ..., i].
#
# Return the distinct difference array of nums.
#
# Note that nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j inclusive.
# Particularly, if i > j then nums[i, ..., j] denotes an empty subarray.

from typing import List
from collections import defaultdict

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        suff_dict = defaultdict(int)
        for i in nums:
            suff_dict[i] += 1

        pref_set = set()
        result = [0] * len(nums)
        for index, i in enumerate(nums):
            pref_set.add(i)
            suff_dict[i] -= 1
            if suff_dict[i] == 0:
                suff_dict.pop(i)
            result[index] = (len(pref_set) - len(suff_dict))

        return result

nums = [1,2,3,4,5]
x = Solution()
print(x.distinctDifferenceArray(nums))