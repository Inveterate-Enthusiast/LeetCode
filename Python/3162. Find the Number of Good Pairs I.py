# You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.
#
# A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).
#
# Return the total number of good pairs.

from typing import List
from itertools import product
from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combs = product(nums1, nums2)
        result = 0
        for i, j in combs:
            if (i % (j * k)) == 0:
                result += 1

        return result

    def numberOfPairs1(self, nums1: List[int], nums2: List[int], k: int) -> int:
        our_dict = defaultdict(int)


nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1
x = Solution()
print(x.numberOfPairs1(nums1, nums2, k))