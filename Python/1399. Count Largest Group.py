# You are given an integer n.
#
# Each number from 1 to n is grouped according to the sum of its digits.
#
# Return the number of groups that have the largest size.

from collections import defaultdict
from functools import reduce

class Solution:
    def countLargestGroup(self, n: int) -> int:
        our_dict = defaultdict(int)
        our_max = 0
        for i in range(1, n + 1):
            x = reduce(lambda acc, x: acc + x, [int(j) for j in str(i)], 0)
            our_dict[x] += 1
            our_max = max(our_max, our_dict[x])

        result = 0
        for key, value in our_dict.items():
            if value == our_max:
                result += 1

        return result

    def countLargestGroup1(self, n: int) -> int:
        our_dict = defaultdict(int)
        our_max = 0
        for i in range(1, n + 1):
            x = sum([int(j) for j in str(i)])
            our_dict[x] += 1
            our_max = max(our_max, our_dict[x])

        result = 0
        for key, value in our_dict.items():
            if value == our_max:
                result += 1

        return result

n = 13
x = Solution()
print(x.countLargestGroup1(n))