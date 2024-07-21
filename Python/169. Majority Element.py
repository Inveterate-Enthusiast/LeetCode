# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.


from typing import List, Optional
from collections import defaultdict
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        _dict = defaultdict(int)
        curLen = len(nums)
        majNumber = math.ceil(curLen / 2)
        for integer in nums:
            _dict[integer] += 1
            if _dict[integer] == majNumber: return integer

        return None

nums = [6,5,5]
X = Solution()
print(X.majorityElement(nums))