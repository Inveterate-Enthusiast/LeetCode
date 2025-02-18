# You are given two integer arrays of equal length target and arr.
# In one step, you can select any non-empty subarray of arr and reverse it.
# You are allowed to make any number of steps.
#
# Return true if you can make arr equal to target or false otherwise.

from typing import List
from collections import defaultdict

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dict_1 = defaultdict(int)
        dict_2 = defaultdict(int)
        for i in target:
            dict_1[i] += 1
        for i in arr:
            dict_2[i] += 1

        return dict_1 == dict_2

target = [1,2,3,4]
arr = [2,4,1,3]
x = Solution()
print(x.canBeEqual(target, arr))