# Given an array of integers arr, return true if and only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n <= 1:
            return False

        prev = 0
        peak = False
        for i in range(1, n):
            if arr[prev] == arr[i]:
                return False
            if prev == 0 and arr[prev] > arr[i]:
                return False
            if i == (n-1) and arr[prev] < arr[i]:
                return False

            if arr[prev] > arr[i]:
                peak = True
            elif peak and arr[prev] < arr[i]:
                return False
            prev = i
        return True

arr = [0,1,2,3,4,5,6,7,8,9]
x = Solution()
print(x.validMountainArray(arr))