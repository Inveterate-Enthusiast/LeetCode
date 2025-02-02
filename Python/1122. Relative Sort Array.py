# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
# Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

from typing import List
from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        our_dict = defaultdict(int)
        for i in arr2:
            our_dict[i] = 0

        rem = list()
        for i in arr1:
            if i in our_dict:
                our_dict[i] += 1
            else:
                rem.append(i)

        result = list()
        for k, v in our_dict.items():
            result.extend([k] * v)
        result.extend(sorted(rem))
        return result

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
x = Solution()
print(x.relativeSortArray(arr1, arr2))