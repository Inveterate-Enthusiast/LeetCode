# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
import numpy as np
import statistics
import bottleneck as bn
import pandas as pd
from numba import njit

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    OurTotalArray = sorted(list(nums1 + nums2))
    if nums1 == nums2:
        OurMedium = (OurTotalArray[len(OurTotalArray)//2]) if len(OurTotalArray)%2!=0 else (((OurTotalArray[len(OurTotalArray)//2-1])+(OurTotalArray[len(OurTotalArray)//2]))/2)
    else:
        OurMedium = (OurTotalArray[len(OurTotalArray)//2]) if len(OurTotalArray)%2!=0 else ((OurTotalArray[len(OurTotalArray)//2-1]) if (OurTotalArray[len(OurTotalArray)//2-1] in nums1)and(OurTotalArray[len(OurTotalArray)//2-1] in nums2) else ((OurTotalArray[len(OurTotalArray)//2]) if (OurTotalArray[len(OurTotalArray)//2] in nums1)and(OurTotalArray[len(OurTotalArray)//2] in nums2) else ((((OurTotalArray[len(OurTotalArray)//2-1])+(OurTotalArray[len(OurTotalArray)//2]))/2))))
    return OurMedium

def findMedianSortedArrays1(nums1: list[int], nums2: list[int]) -> float:
    return np.median(nums1 + nums2)

def findMedianSortedArrays2(nums1: list[int], nums2: list[int]) -> float:
    return statistics.median(nums1 + nums2)

def findMedianSortedArrays3(nums1: list[int], nums2: list[int]) -> float: # медленный
    return pd.Series(nums1 + nums2).median()

def findMedianSortedArrays4(nums1: list[int], nums2: list[int]) -> float:
    return bn.median(nums1 + nums2)

@njit
def findMedianSortedArrays5(nums1: list[int], nums2: list[int]) -> float:
    combined = np.array(nums1 + nums2)
    combined.sort()
    n = len(combined)
    if n % 2 == 0:
        return (combined[n // 2 - 1] + combined[n // 2]) / 2
    else:
        return combined[n // 2]

L1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
L2 = [0,6]
L = findMedianSortedArrays4(L1, L2)
print(L)