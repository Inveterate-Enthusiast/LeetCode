# Given an array arr of integers, check if there exist two indices i and j such that :
#
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

from typing import List
from collections import defaultdict

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        our_dict = defaultdict(lambda: [float("inf"), float("-inf")])
        for index, a in enumerate(arr):
            our_dict[a][0] = min(our_dict[a][0], index) if our_dict[a][0] else index
            our_dict[a][1] = max(our_dict[a][1], index) if our_dict[a][1] else index

        for index, a in enumerate(arr):
            if (a * 2) in our_dict and (our_dict[(a * 2)][0] != index or our_dict[(a * 2)][1] != index):
                return True

        return False

    def checkIfExist1(self, arr: List[int]) -> bool:
        our_set = set()
        for a in arr:
            if (a * 2) in our_set or (a / 2) in our_set:
                return True
            our_set.add(a)
        return False


arr = [10,2,5,3]
x = Solution()
print(x.checkIfExist(arr))