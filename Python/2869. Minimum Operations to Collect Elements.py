# You are given an array nums of positive integers and an integer k.
#
# In one operation, you can remove the last element of the array and add it to your collection.
#
# Return the minimum number of operations needed to collect elements 1, 2, ..., k.

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        set_origin = set([i for i in range(1, k+1)])
        set_temp = set()
        result = 0
        for i in range(len(nums)-1, -1, -1):
            result += 1
            if nums[i] in set_origin:
                set_temp.add(nums[i])
            if set_origin == set_temp:
                return result
        return 0

nums = [3,1,5,4,2]
k = 2
x = Solution()
print(x.minOperations(nums, k))