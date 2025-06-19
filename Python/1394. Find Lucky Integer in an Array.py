# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
#
# Return the largest lucky integer in the array. If there is no lucky integer return -1.

from typing import List
from collections import defaultdict

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        our_dict = defaultdict(int)
        for i in arr:
            our_dict[i] += 1

        result = float("-inf")
        for num, freq in our_dict.items():
            if num == freq:
                result = max(result, num)

        return result if result != float("-inf") else (-1)


arr = [2,2,3,4]
x = Solution()
print(x.findLucky(arr))