# You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:
#
# answer1 : the number of indices i such that nums1[i] exists in nums2.
# answer2 : the number of indices i such that nums2[i] exists in nums1.
# Return [answer1,answer2].

from typing import List
from collections import defaultdict

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1, dict2 = defaultdict(int), defaultdict(int)
        result = [0] * 2
        for i in nums1:
            dict1[i] += 1

        for i in nums2:
            dict2[i] += 1

        for value, count in dict1.items():
            if value in dict2:
                result[0] += count
                result[1] += dict2[value]

        return result

    def findIntersectionValues1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        result = [0] * 2
        for i in nums1:
            if i in set2:
                result[0] += 1

        for i in nums2:
            if i in set1:
                result[1] += 1

        return result


nums1 = [2,3,2]
nums2 = [1,2]
x = Solution()
print(x.findIntersectionValues1(nums1, nums2))