# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
#
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
#
# Return any answer array that satisfies this condition.

from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        list_even, list_odd = list(), list()
        for num in nums:
            if (num % 2) == 0:
                list_even.append(num)
            else:
                list_odd.append(num)

        i_even, i_odd = 0, 0
        for i in range(len(nums)):
            if (i == 0) or ((i % 2) == 0):
                nums[i] = list_even[i_even]
                i_even += 1
            else:
                nums[i] = list_odd[i_odd]
                i_odd += 1

        return nums

    def sortArrayByParityII1(self, nums: List[int]) -> List[int]:
        i_even, i_odd = 0, 1
        result = [0] * len(nums)
        for num in nums:
            if (num % 2) == 0:
                result[i_even] = num
                i_even += 2
            else:
                result[i_odd] = num
                i_odd += 2

        return result

nums = [4,2,5,7]
x = Solution()
print(x.sortArrayByParityII1(nums))