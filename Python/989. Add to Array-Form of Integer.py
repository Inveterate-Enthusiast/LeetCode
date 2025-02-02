# The array-form of an integer num is an array representing its digits in left to right order.
#
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = list()
        n = len(num)-1
        k_str = str(k)
        kk = len(k_str)-1
        x_rem = 0
        while n >= 0 or kk >= 0:
            if kk >= 0 and n >= 0:
                x_add = (num[n] + int(k_str[kk]) + x_rem) % 10
                x_rem = (num[n] + int(k_str[kk]) + x_rem) // 10
            elif n >= 0:
                x_add = (num[n] + x_rem) % 10
                x_rem = (num[n] + x_rem) // 10
            elif kk >= 0:
                x_add = (int(k_str[kk]) + x_rem) % 10
                x_rem = (int(k_str[kk]) + x_rem) // 10
            result.append(x_add)
            n -= 1
            kk -= 1
        else:
            if x_rem: result.append(x_rem)

        return result[::-1]

num = [0]
k = 10000
x = Solution()
print(x.addToArrayForm(num, k))