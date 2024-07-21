# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
#
# After doing so, return the array.
from typing import List, Optional
from collections import deque

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return list()
        arrLen = len(arr)
        _dict = {i: -1 for i in range(arrLen)}

        for i in range(arrLen-2, -1, -1):
            _dict[i] = max(_dict[i+1], arr[i+1])

        for i, _ in enumerate(arr):
            arr[i] = _dict[i]

        return arr

    def replaceElements1(self, arr: List[int]) -> List[int]:
        if not arr:
            return list()

        arrLen = len(arr)
        newArr = [-1] * arrLen
        maxVal = (-1)
        for i in range(arrLen-2, -1, -1):
            maxVal = maxVal if maxVal >= arr[i+1] else arr[i+1]
            newArr[i] = maxVal

        return newArr

    def replaceElements2(self, arr: List[int]) -> List[int]:
        if not arr:
            return list()

        arrLen = len(arr)
        maxVal = (-1)
        for i in range(arrLen-2, -2, -1):
            val, arr[i+1] = arr[i+1], maxVal
            maxVal = max(maxVal, val)
        return arr

arr = [17,18,5,4,6,1]
X = Solution()
print(X.replaceElements2(arr))

