# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing
# only 1's in the resulting array. Return 0 if there is no such subarray.

def longestSubarray1(nums: list[int]) -> int:
    OurResultSize = OurCurrentSize = OurZero = leftIndex = 0
    for rightIndex in range(len(nums)):
        OurCurrentSize = (OurCurrentSize + 1) if nums[rightIndex] == 1 else OurCurrentSize
        OurZero = (OurZero + 1) if nums[rightIndex] == 0 else OurZero
        while leftIndex <= rightIndex and OurZero > 1:
            OurCurrentSize = (OurCurrentSize - 1) if nums[leftIndex] == 1 else OurCurrentSize
            OurZero = (OurZero - 1) if nums[leftIndex] == 0 else OurZero
            leftIndex += 1
        if leftIndex <= rightIndex and OurZero <= 1:
            OurResultSize = max(OurResultSize, OurCurrentSize if OurZero == 1 else OurCurrentSize-1)
    return OurResultSize

V = [1,1,1]
print(longestSubarray1(V))