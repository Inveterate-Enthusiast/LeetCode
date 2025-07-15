# You have an array of floating point numbers averages which is initially empty.
# You are given an array nums of n integers where n is even.
#
# You repeat the following procedure n / 2 times:
#
# Remove the smallest element, minElement, and the largest element maxElement, from nums.
# Add (minElement + maxElement) / 2 to averages.
# Return the minimum element in averages.

from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        result = float("inf")
        while nums:
            _min, _max = nums.pop(0), nums.pop(-1)
            result = min(result, (_min + _max) / 2)
        return result

nums = [7,8,3,4,15,13,4,1]
x = Solution()
print(x.minimumAverage(nums))