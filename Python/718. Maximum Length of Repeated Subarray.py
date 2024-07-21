# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
from typing import List, Optional

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int: # некорректно работает
        len1 = len(nums1); len2 = len(nums2)
        OurDP = [[0 for i in range(len2+1)] for _ in range(len1+1)]

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if nums1[i-1] == nums2[j-1]:
                    OurDP[i][j] = 1 + OurDP[i-1][j-1]
                else:
                    OurDP[i][j] = max(
                        OurDP[i-1][j],
                        OurDP[i][j-1]
                    )

        return OurDP[-1][-1]

    def findLength1(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0

        len1 = len(nums1); len2 = len(nums2)
        OurDP = [[0] * (len2+1) for _ in range(len1 + 1)]
        OurMax = 0

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    OurDP[i][j] = 1 + OurDP[i - 1][j - 1]
                    OurMax = max(OurMax, OurDP[i][j])

        return OurMax

nums1 = [0,1,1,1,1]; nums2 = [1,0,1,0,1]
X = Solution()
print(X.findLength1(nums1, nums2))

