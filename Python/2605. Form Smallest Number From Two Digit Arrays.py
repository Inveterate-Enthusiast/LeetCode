# Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.

from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        set_1, min_1 = set(), None
        for i in nums1:
            min_1 = i if min_1 is None else min(min_1, i)
            set_1.add(i)

        set_2, min_2 = set(), None
        for i in nums2:
            min_2 = i if min_2 is None else min(min_2, i)
            set_2.add(i)

        set_common = set_1 & set_2
        if len(set_common) == 0:
            return int(str(min([min_1, min_2])) + str(max([min_1, min_2])))
        else:
            return min(list(set_common))


nums1 = [4,1,3]
nums2 = [5,7]
x = Solution()
print(x.minNumber(nums1, nums2))