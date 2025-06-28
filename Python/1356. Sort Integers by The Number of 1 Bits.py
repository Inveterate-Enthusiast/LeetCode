# You are given an integer array arr. Sort the integers in the array in ascending order
# by the number of 1's in their binary representation and in case of two or more integers
# have the same number of 1's you have to sort them in ascending order.
#
# Return the array after sorting it.

from typing import List
from functools import reduce

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        n = len(arr)
        temp = [0] * n
        for i in range(n):
            _bit = reduce(lambda acc, x: acc + int(x), bin(arr[i])[2:], 0)
            temp[i] = _bit

        return [i for i, j in sorted(zip(arr, temp), key=lambda x: (x[1], x[0]))]



arr = [0,1,2,3,4,5,6,7,8]
x = Solution()
print(x.sortByBits(arr))