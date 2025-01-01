# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Given an integer array nums, return the length of its longest harmonious
# subsequence
#  among all its possible subsequences.
from typing import List
from collections import defaultdict

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        left = 0
        result = 0
        nums.sort()
        for right in range(len(nums)):
            while (left < right) and (nums[right] - nums[left]) > 1:
                left += 1
            if (nums[right] - nums[left]) == 1:
                result = max(result, right - left + 1)
        return result

    def findLHS1(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        result = 0
        for num in nums:
            our_dict[num] += 1

        for num in our_dict:
            if num + 1 in our_dict:
                result = max(result, our_dict[num] + our_dict[num + 1])

        return result

nums = [1,3,2,2,5,2,3,7]
x = Solution()
print(x.findLHS1(nums))