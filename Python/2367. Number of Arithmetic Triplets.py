# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
# A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
#
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

from typing import List
from itertools import combinations

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        combs = combinations(nums, 3)
        our_set = set()
        result = 0
        for i, j, k in combs:
            if (((j - i) == diff) and ((k - j) == diff)) and (not tuple([i, j, j]) in our_set):
                result += 1
                our_set.add(tuple([i, j, k]))

        return result

nums = [0,1,4,6,7,10]
diff = 3
x = Solution()
print(x.arithmeticTriplets(nums, diff))