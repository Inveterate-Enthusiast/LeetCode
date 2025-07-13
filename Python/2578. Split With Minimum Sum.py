# Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
#
# The concatenation of num1 and num2 is a permutation of num.
# In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal
# to the number of occurrences of that digit in num.
# num1 and num2 can contain leading zeros.
# Return the minimum possible sum of num1 and num2.
#
# Notes:
#
# It is guaranteed that num does not contain any leading zeros.
# The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.

class Solution:
    def splitNum(self, num: int) -> int:
        num_str = [int(i) for i in sorted(str(num))]
        x1, x2 = 0, 0
        for index, i in enumerate(num_str, start=1):
            if (index % 2) != 0:
                x1 = (x1 * 10) + i
            else:
                x2 = (x2 * 10) + i

        return x1 + x2

num = 4325
x = Solution()
print(x.splitNum(num))