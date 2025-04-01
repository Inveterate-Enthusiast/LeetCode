# You are given an array of distinct integers arr and an array of integer arrays pieces,
# where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order.
# However, you are not allowed to reorder the integers in each array pieces[i].
#
# Return true if it is possible to form the array arr from pieces. Otherwise, return false.

from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces_set = {tuple(i) for i in pieces}
        n = len(arr)

        left = 0
        for right in range(n):
            if (x := tuple(arr[left:right+1])) in pieces_set:
                pieces_set.remove(x)
                left = right + 1
            else:
                if right == (n - 1): return False

        return not pieces_set

arr = [15,88]
pieces = [[88],[15]]
x = Solution()
print(x.canFormArray(arr, pieces))