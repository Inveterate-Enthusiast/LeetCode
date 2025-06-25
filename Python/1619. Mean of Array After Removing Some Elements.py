# Given an integer array arr, return the mean of the remaining integers
# after removing the smallest 5% and the largest 5% of the elements.
#
# Answers within 10-5 of the actual answer will be considered accepted.

from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        temp_arr = sorted(arr)
        n = len(temp_arr)
        result = [temp_arr[i] for i in range(n) if (i >= int(0.05 * n)) and (i < int(0.95 * n))]
        return sum(result) / len(result)


arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
x = Solution()
print(x.trimMean(arr))