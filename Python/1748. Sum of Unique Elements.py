# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
#
# Return the sum of all the unique elements of nums.

from typing import List
from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        for n in nums:
            our_dict[n] += 1

        result = 0
        for k, v in our_dict.items():
            if v == 1:
                result += k

        return result

nums = [1,2,3,2]
x = Solution()
print(x.sumOfUnique(nums))