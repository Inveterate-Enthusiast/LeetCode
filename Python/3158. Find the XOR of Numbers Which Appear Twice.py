# You are given an array nums, where each number in the array appears either once or twice.
#
# Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.

from typing import List
from collections import defaultdict

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        for i in nums:
            our_dict[i] += 1

        result = 0
        for k, v in our_dict.items():
            if v == 2:
                result ^= k

        return result


nums = [1,2,1,3]
x = Solution()
print(x.duplicateNumbersXOR(nums))