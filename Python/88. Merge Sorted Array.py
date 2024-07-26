# You are given two integer arrays nums1 and nums2,
# sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function,
# but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy1 = nums1.copy()
        index = 0
        left = right = 0
        while left < m or right < n:
            if (left < m and right < n and copy1[left] <= nums2[right]) or right >= n:
                nums1[index] = copy1[left]; left += 1
            else:
                nums1[index] = nums2[right]; right += 1
            index += 1



nums1 = [1]; m = 1; nums2 = []; n = 0
X = Solution()
X.merge(nums1, m, nums2, n)
print(nums1)