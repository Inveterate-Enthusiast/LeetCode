# You are given an array of integers nums of length n.
#
# The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.
#
# You need to divide nums into 3 disjoint contiguous subarrays.
#
# Return the minimum possible sum of the cost of these subarrays.

from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n1, n2, n3 = nums[0], float("inf"), float("inf")
        for n in nums[1:]:
            if n < n2:
                n3, n2 = n2, n
            elif n < n3:
                n3 = n
        return sum([n1, n2, n3])

nums = [1,2,3,12]
x = Solution()
print(x.minimumCost(nums))