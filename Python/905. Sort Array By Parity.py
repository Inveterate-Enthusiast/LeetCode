# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#
# Return any array that satisfies this condition.

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_ar = list()
        odd_ar = list()
        for num in nums:
            if (num % 2) == 0:
                even_ar.append(num)
            else:
                odd_ar.append(num)
        return even_ar + odd_ar

nums = [3,1,2,4]
x = Solution()
print(x.sortArrayByParity(nums))