# You are given two integer arrays nums1 and nums2 where nums2 is an anagram of nums1. Both arrays may contain duplicates.
#
# Return an index mapping array mapping from nums1 to nums2 where mapping[i] = j means the ith element in nums1 appears in nums2 at index j.
# If there are multiple answers, return any of them.
#
# An array a is an anagram of an array b means b is made by randomizing the order of the elements in a.
from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        our_dict = dict()
        for index, num in enumerate(nums2):
            if not num in our_dict: our_dict[num] = index

        result = list()
        for num in nums1:
            result.append(our_dict[num])

        return result

nums1 = [12,28,46,32,50]; nums2 = [50,12,32,46,28]
x = Solution()
print(x.anagramMappings(nums1, nums2))