# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
#
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr_sort = sorted(arr)
        n = len(arr)
        our_min = float("inf")
        for i in range(1,n):
            our_min = min(our_min, (arr_sort[i] - arr_sort[i-1]))

        result = list()
        for i in range(1, n):
            if (arr_sort[i] - arr_sort[i-1]) == our_min:
                result.append([arr_sort[i-1], arr_sort[i]])

        return result

arr = [4,2,1,3]
x = Solution()
print(x.minimumAbsDifference(arr))