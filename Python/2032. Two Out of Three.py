# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present
# in at least two out of the three arrays. You may return the values in any order.

from typing import List
import itertools

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        our_list = [set(i) for i in [nums1, nums2, nums3]]
        result = set()
        for i in itertools.combinations(our_list, 2):
            result = result.union(i[0].intersection(i[1]))
        return list(result)

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
x = Solution()
print(x.twoOutOfThree(nums1, nums2, nums3))