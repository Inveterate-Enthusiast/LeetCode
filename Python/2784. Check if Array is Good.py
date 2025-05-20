# You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].
#
# base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once,
# plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
#
# Return true if the given array is good, otherwise return false.
#
# Note: A permutation of integers represents an arrangement of these numbers.

from typing import List
from collections import defaultdict

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        our_dict = defaultdict(int)
        our_set = set([i for i in range(1, n+1)])

        for num in nums:
            our_dict[num] += 1
            our_set.discard(num)
            if num != n and our_dict[num] > 1:
                return False

        return (our_dict[n] == 2) and (len(our_set) == 0)

    def isGood1(self, nums: List[int]) -> bool:
        our_dict = defaultdict(int)
        n = nums[0]
        for num in nums:
            our_dict[num] += 1
            n = max(n, num)

        for num in range(1, n):
             if our_dict[num] != 1:
                 return False

        return our_dict[n] == 2

nums = [9, 9]
x = Solution()
print(x.isGood(nums))