# You are given an integer array nums. You have to find the maximum sum of a pair of numbers
# from nums such that the largest digit in both numbers is equal.
#
# For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.
#
# Return the maximum sum or -1 if no such pair exists.

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        our_dict = dict()
        result = (-1)
        for num in nums:
            cur_max = max(list(map(int, str(num))))
            if cur_max in our_dict:
                result = max(result, (num + our_dict[cur_max]))
                our_dict[cur_max] = max(our_dict[cur_max], num)
            else:
                our_dict[cur_max] = num
        return result

nums = [2536,1613,3366,162]
x = Solution()
print(x.maxSum(nums))