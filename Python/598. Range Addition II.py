# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y]
# should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
#
# Count and return the number of maximum integers in the matrix after performing all the operations.
from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_m = m
        min_n = n
        for op in ops:
            min_m, min_n = min(min_m, op[0]), min(min_n, op[1])
        return min_m * min_n

m = 18; n = 3; ops = [[16,1],[14,3],[14,2],[4,1],[10,1],[11,1],[8,3],[16,2],[13,1],[8,3],[2,2],[9,1],[3,1],[2,2],[6,3]]
x = Solution()
print(x.maxCount(m, n, ops))