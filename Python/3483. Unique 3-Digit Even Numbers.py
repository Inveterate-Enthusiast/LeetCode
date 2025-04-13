# You are given an array of digits called digits. Your task is to determine the number
# of distinct three-digit even numbers that can be formed using these digits.
#
# Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

from typing import List
from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        combs = permutations(digits, 3)
        result = set()
        for i in combs:
            if (i[0] != 0) and (((x := int("".join(map(str, i)))) % 2) == 0):
                result.add(x)
        return len(result)

    def totalNumbers1(self, digits: List[int]) -> int:
        combs = permutations(digits, 3)
        result = set()
        for i in combs:
            if (i[0] != 0) and ((i[2] % 2) == 0):
                result.add(i)
        return len(result)

digits = [1,2,3,4]
x = Solution()
print(x.totalNumbers1(digits))