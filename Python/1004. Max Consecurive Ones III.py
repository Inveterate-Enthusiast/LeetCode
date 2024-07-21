# Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
from typing import List, Optional

def longestOnes1(nums: list[int], k: int) -> int:
    OurResultNumber = NumOne = NumZero = 0
    leftIndex = 0
    for rightIndex in range(len(nums)):
        NumOne = (NumOne + 1) if nums[rightIndex] == 1 else NumOne
        NumZero = (NumZero + 1) if nums[rightIndex] == 0 else NumZero
        while leftIndex <= rightIndex and NumZero > k:
            NumOne = (NumOne - 1) if nums[leftIndex] == 1 else NumOne
            NumZero = (NumZero - 1) if nums[leftIndex] == 0 else NumZero
            leftIndex += 1
        if leftIndex <= rightIndex and NumZero <= k:
            OurResultNumber = max(OurResultNumber, NumOne + NumZero)

    return OurResultNumber


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLength = 0
        zeroCount = 0
        for right, value in enumerate(nums):
            if not value:
                zeroCount += 1

            while left <= right and zeroCount > k:
                left += 1
                if left > 0 and not nums[left-1]: zeroCount -= 1

            maxLength = max(maxLength, (right - left + 1))

        return maxLength



V = [1,1,1,0,0,0,1,1,1,1,0]; k = 1
X = Solution()
print(X.longestOnes(V, k))
