# Given an array nums, you can perform the following operation any number of times:
#
# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.
#
# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

from typing import List

class Solution:
    def check_descrising(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                return False
        return True

    def minimumPairRemoval(self, nums: List[int]) -> int:
        result = 0
        temp = nums
        while not self.check_descrising(temp):
            n = len(temp)
            cur_min = float("inf")
            cur_inx = None
            for i in range(1, n):
                if (x := (temp[i] + temp[i-1])) < cur_min:
                    cur_min = x
                    cur_inx = i
            temp = temp[:(cur_inx - 1)] + [cur_min] + temp[(cur_inx + 1):]
            result += 1
        return result



nums = [2,2,-1,3,-2,2,1,1,1,0,-1]
x = Solution()
print(x.minimumPairRemoval(nums))