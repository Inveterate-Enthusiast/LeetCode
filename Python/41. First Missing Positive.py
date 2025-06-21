# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
#
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int: # Memory Limit Exceeded
        our_max = max(nums)
        our_max = our_max if our_max > 0 else 0
        result = our_max + 1 if our_max else 1
        try:
            return ({i for i in range(1, our_max+1)}.difference(set(nums))).pop()
        except:
            return result

    def firstMissingPositive1(self, nums: List[int]) -> int:
        our_min = float("inf")
        our_max = float("-inf")
        for num in set(nums):
            if num > 0:
                our_min = min(our_min, num)
            our_max = max(our_max, num)
        if our_min > 1:
            return 1

        our_max = our_max if our_max > 0 else 0
        result = our_max + 1 if our_max else 1

        n = len(nums)

        for idx, num in enumerate(nums):
            while (num > 0) and (num <= n) and (num != nums[num-1]):
                nums[idx], nums[num-1] = nums[num-1], nums[idx]
                num = nums[idx]

        for idx, num in enumerate(nums, 1):
            if idx != num:
                return idx

        return result

nums = [-3,9,16,4,5,16,-4,9,26,2,1,19,-1,25,7,22,2,-7,14,2,5,-6,1,17,3,24,-4,17,15]
x = Solution()
print(x.firstMissingPositive1(nums))