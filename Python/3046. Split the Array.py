# You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2 such that:
#
# nums1.length == nums2.length == nums.length / 2.
# nums1 should contain distinct elements.
# nums2 should also contain distinct elements.
# Return true if it is possible to split the array, and false otherwise.

from typing import List
from collections import defaultdict

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if (len(nums) % 2) != 0:
            return False

        our_dict = defaultdict(int)
        for num in nums:
            our_dict[num] += 1

        for num, freq in our_dict.items():
            if freq > 2:
                return False

        return True

nums = [1,1,2,2,3,4]
x = Solution()
print(x.isPossibleToSplit(nums))