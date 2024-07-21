# Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

from typing import List, Optional

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = 0
        left = 0
        zerroCount = 0
        for right, value in enumerate(nums):
            if not value:
                zerroCount += 1

            while left <= right and zerroCount > 1:
                left += 1
                if left > 0 and not nums[left-1]: zerroCount -= 1

            maxLength = max(maxLength, (right - left + 1))

        return maxLength




nums = [1,0,1,1,0]
X = Solution()
print(X.findMaxConsecutiveOnes(nums))
