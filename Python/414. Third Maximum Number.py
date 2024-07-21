# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

from typing import List, Optional
from collections import deque

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return None

        _queue = deque(maxlen=3)
        nums = sorted(nums, reverse=True)
        _queue.append(nums[0])
        for i in range(1, len(nums)):
            if len(_queue) == 3:
                return _queue[-1]
            if nums[i] < _queue[-1]:
                _queue.append(nums[i])

        return _queue[-1] if len(_queue) == 3 else _queue[0]

    def thirdMax1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums = {i:i for i in nums}
        ans = None; biggest = float("-inf")
        for i in range(3):
            if not nums:
                return biggest
            biggest = max(biggest, (ans := nums.pop(max(nums))))

        return ans




nums = [3,2,1]
X = Solution()
print(X.thirdMax1(nums))

