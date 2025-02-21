# You are given an integer array digits, where each element is a digit. The array may contain duplicates.
#
# You need to find all the unique integers that follow the given requirements:
#
# The integer consists of the concatenation of three elements from digits in any arbitrary order.
# The integer does not have leading zeros.
# The integer is even.
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
#
# Return a sorted array of the unique integers.

from typing import List
import itertools

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        combs = list(itertools.permutations(digits, 3))
        result = set()
        for i in combs:
            if not (i[0] == 0) and (i[2] % 2 == 0):
                x = int("".join(map(str, i)))
                result.add(x)

        return sorted(list(result))



digits = [2,1,3,0]
x = Solution()
print(x.findEvenNumbers(digits))