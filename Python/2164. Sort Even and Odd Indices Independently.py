# You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:
#
# Sort the values at odd indices of nums in non-increasing order.
# For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.
# Sort the values at even indices of nums in non-decreasing order.
# For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.
# Return the array formed after rearranging the values of nums.

from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        list_even, list_odd = sorted([nums[i] for i in range(n) if (i % 2) == 0]), sorted([nums[i] for i in range(n) if (i % 2) != 0], reverse=True)

        i_even, i_odd = 0, 0
        result = list()
        for i in range(n):
            if (i % 2) == 0:
                result.append(list_even[i_even])
                i_even += 1
            else:
                result.append(list_odd[i_odd])
                i_odd += 1

        return result


nums = [4,1,2,3]
x = Solution()
print(x.sortEvenOdd(nums))