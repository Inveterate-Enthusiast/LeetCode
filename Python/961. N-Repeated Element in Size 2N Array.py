# You are given an integer array nums with the following properties:
#
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

from typing import List
from collections import defaultdict

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        our_dict = defaultdict(int)
        our_set =  set()
        for num in nums:
            our_dict[num] += 1
            if our_dict[num] == n:
                our_set.add(num)
            elif num in our_set:
                our_set.remove(num)
        return our_set.pop()

nums = [1,2,3,3]
x = Solution()
print(x.repeatedNTimes(nums))