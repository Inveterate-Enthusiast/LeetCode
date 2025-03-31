# Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
# If multiple values have the same frequency, sort them in decreasing order.
#
# Return the sorted array.

from typing import List
from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        our_dict = defaultdict(int)
        for i in nums:
            our_dict[i] += 1

        pos_dict = defaultdict(list)
        for key, value in our_dict.items():
            pos_dict[value].extend([key] * value)

        result = list()
        for i in range(len(nums)+1):
            result.extend(sorted(pos_dict[i], reverse=True))

        return result

nums = [-3]
x = Solution()
print(x.frequencySort(nums))