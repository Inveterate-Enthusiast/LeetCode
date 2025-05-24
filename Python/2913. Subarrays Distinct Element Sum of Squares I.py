# You are given a 0-indexed integer array nums.
#
# The distinct count of a subarray of nums is defined as:
#
# Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length.
# Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
# Return the sum of the squares of distinct counts of all subarrays of nums.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for left in range(n):
            our_set = set()
            for right in range(left, n):
                our_set.add(nums[right])
                result += len(our_set) ** 2

        return result

nums = [1,2,1]
x = Solution()
print(x.sumCounts(nums))