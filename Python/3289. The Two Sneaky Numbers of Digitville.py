# In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1.
# Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time,
# making the list longer than usual.
#
# As the town detective, your task is to find these two sneaky numbers. Return an array of size
# two containing the two numbers (in any order), so peace can return to Digitville.

from typing import List
from collections import defaultdict

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        our_dict = defaultdict(int)
        result = list()
        for i in nums:
            our_dict[i] += 1
            if our_dict[i] > 1: result.append(i)

        return result

nums = [0,3,2,1,3,2]
x = Solution()
print(x.getSneakyNumbers(nums))