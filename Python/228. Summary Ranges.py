# You are given a sorted unique integer array nums.
#
# A range [a,b] is the set of all integers from a to b (inclusive).
#
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
#
# "a->b" if a != b
# "a" if a == b
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = right = nums[0] if nums else 0
        result = [[nums[0]]] if nums else list()
        for num in nums:
            if (num - right) > 1:
                result[-1] = result[-1] if (left == right) else [result[-1][0], right]
                result.append([num])
                left = num
            else:
                result[-1] = result[-1] if (num == right) else [result[-1][0], num]
            right = num
        return [f"{i[0]}->{i[1]}" if len(i) > 1 else f"{i[0]}" for i in result]

X = Solution()
nums = [0,2,3,4,6,8,9]
print(X.summaryRanges(nums))