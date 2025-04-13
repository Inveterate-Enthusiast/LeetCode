# You are given an integer array nums and an integer k.
#
# An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.
#
# Return the largest almost missing integer from nums. If no such integer exists, return -1.
#
# A subarray is a contiguous sequence of elements within an array.

from typing import List
from collections import defaultdict


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        our_dict = defaultdict(int)
        n = len(nums)
        for i in range(k):
            our_dict[nums[i]] = max(our_dict[nums[i]], min((i + 1), (n - k + 1)))

        for i in range(k, n):
            our_dict[nums[i]] += k if (n - i) > k else (n - i)

        result = None
        for key, value in our_dict.items():
            if value == 1:
                result = key if result is None else max(result, key)

        return (-1) if result is None else result




nums = [3,0,12,7,1,11]
k = 6
x = Solution()
print(x.largestInteger(nums, k))