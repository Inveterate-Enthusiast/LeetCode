# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.
#
# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
#
# Return the shortest sorted list of ranges that exactly covers all the missing numbers.
# That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.
from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = list()
        for num in nums:
            if num > lower:
                result.append([lower, num-1])
            lower = num + 1
        if lower <= upper:
            result.append([lower, upper])
        return result


X = Solution()
nums, lower, upper = [0, 1, 3, 50, 75], 0, 99
print(X.findMissingRanges(nums, lower, upper))