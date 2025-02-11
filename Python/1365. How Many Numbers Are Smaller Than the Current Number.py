# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
#
# Return the answer in an array.

from typing import List
from collections import defaultdict

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        our_dict = defaultdict(int)
        prev_n = None
        counter = 0
        for n in sorted(nums):
            if not prev_n is None and prev_n != n:
                our_dict[n] = counter
            else:
                our_dict[n] = our_dict.get(n, 0)
            counter += 1
            prev_n = n

        result = [0] * len(nums)
        for index, n in enumerate(nums):
            result[index] = our_dict[n]

        return result





nums = [5,0,10,0,10,6]
x = Solution()
print(x.smallerNumbersThanCurrent(nums))