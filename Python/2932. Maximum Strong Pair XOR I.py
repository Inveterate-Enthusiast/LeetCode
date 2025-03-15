# You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:
#
# |x - y| <= min(x, y)
# You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.
#
# Return the maximum XOR value out of all possible strong pairs in the array nums.
#
# Note that you can pick the same integer twice to form a pair.

from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        if n <= 1:
            return result

        left, right = 0, 0
        nums_new = sorted(nums)
        while right < n:
            while (left < n) and ((nums_new[left] * 2) < nums_new[right]):
                left += 1

            left_new = left
            while left_new < right:
                if abs(nums_new[left_new] - nums_new[right]) <= nums_new[left_new]:
                    result = max(result, nums_new[left_new] ^ nums_new[right])
                left_new += 1

            right += 1

        return result

nums = [1,2,3,4,5]
x = Solution()
print(x.maximumStrongPairXor(nums))