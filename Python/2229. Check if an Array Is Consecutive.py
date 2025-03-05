# Given an integer array nums, return true if nums is consecutive, otherwise return false.
#
# An array is consecutive if it contains every number in the range [x, x + n - 1] (inclusive),
# where x is the minimum number in the array and n is the length of the array.

from typing import List

class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        our_min = float("inf")
        for num in nums:
            our_min = min(our_min, num)

        our_set = {i for i in range(our_min, our_min + len(nums))}
        for num in nums:
            if num in our_set:
                our_set.remove(num)

        return not our_set

    def isConsecutive1(self, nums: List[int]) -> bool:
        our_min = float("inf")
        our_set = set()
        for num in nums:
            our_min = min(our_min, num)
            our_set.add(num)

        true_set = {i for i in range(our_min, our_min + len(nums))}
        result = our_set ^ true_set
        return not result

nums = [1,3,4,2]
x = Solution()
print(x.isConsecutive1(nums))