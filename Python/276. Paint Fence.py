# You are painting a fence of n posts with k different colors. You must paint the posts following these rules:
#
# Every post must be painted exactly one color.
# There cannot be three or more consecutive posts with the same color.
# Given the two integers n and k, return the number of ways you can paint the fence.
from typing import Optional, List
from collections import defaultdict

class Solution:
    def numWays(self, n: int, k: int) -> int: # вариант рабочий, но медленный
        self.count = 0

        def helper(nth: Optional[int], prev_prev: Optional[int], prev: Optional[int]):
            if nth == n:
                self.count += 1
                return

            for i in range(1, k+1):
                if i != prev or prev_prev != prev:
                    helper(nth + 1, prev, i)

        helper(0, None, None)

        return self.count

    def numWays1(self, n: int, k: int) -> int:
        self._dict = defaultdict(int)
        self._dict[1] = k
        self._dict[2] = k**2

        def helper(nth: int) -> int:
            if nth < 1: return 0
            if (kth := self._dict.get(nth, None)) is not None: return kth

            kth = (helper(nth-1) + helper(nth-2)) * (k-1)
            self._dict[nth] = kth

            return kth

        return helper(n)

n = 3; k = 2
X = Solution()
print(X.numWays1(n, k))
