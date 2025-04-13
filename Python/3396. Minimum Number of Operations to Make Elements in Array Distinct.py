# You are given an integer array nums. You need to ensure that the elements in the array are distinct.
# To achieve this, you can perform the following operation any number of times:
#
# Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
# Note that an empty array is considered to have distinct elements. Return the minimum number of operations
# needed to make the elements in the array distinct.

from typing import List
from collections import defaultdict

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        our_set = set()
        n = len(nums)
        for i in nums:
            our_dict[i] += 1
            if our_dict[i] > 1:
                our_set.add(i)

        left, right = 0, 3
        result = 0
        while len(our_set):
            for i in range(left, min(right, n)):
                our_dict[nums[i]] -= 1
                if our_dict[nums[i]] <= 1: our_set.discard(nums[i])
            left = right
            right += 3
            result += 1
        return result



nums = [1,2,3,4,2,3,3,5,7]
x = Solution()
print(x.minimumOperations(nums))