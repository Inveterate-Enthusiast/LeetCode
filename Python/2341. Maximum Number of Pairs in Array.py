# You are given a 0-indexed integer array nums. In one operation, you may do the following:
#
# Choose two integers in nums that are equal.
# Remove both integers from nums, forming a pair.
# The operation is done on nums as many times as possible.
#
# Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1]
# is the number of leftover integers in nums after doing the operation as many times as possible.

from typing import List
from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        our_dict = defaultdict(int)
        for i in nums:
            our_dict[i] += 1

        result = [0, 0]
        for key, value in our_dict.items():
            result[0] += value // 2
            result[1] += value % 2

        return result

nums = [1,3,2,1,3,2,2]
x = Solution()
print(x.numberOfPairs(nums))