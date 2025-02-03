# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

from functools import reduce

class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 9:
            n = reduce(lambda acc, x: acc + x**2, map(int, [i for i in str(n)]), 0)
        return n == 1 or n == 7

n = 2
x = Solution()
print(x.isHappy(n))