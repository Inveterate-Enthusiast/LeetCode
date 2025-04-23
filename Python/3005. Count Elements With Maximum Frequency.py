# You are given an array nums consisting of positive integers.
#
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
#
# The frequency of an element is the number of occurrences of that element in the array.

from typing import List
from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        our_max = 0
        for i in nums:
            our_dict[i] += 1
            our_max = max(our_max, our_dict[i])

        result = 0
        for i, value in our_dict.items():
            if value == our_max:
                result += value

        return result

nums = [1,2,2,3,1,4]
x = Solution()
print(x.maxFrequencyElements(nums))