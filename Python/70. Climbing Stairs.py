# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
from collections import deque, defaultdict
def climbStairs1(n: int) -> int:
    OurWays = [0, 1] + ([0] * (n))
    for i in range(2, len(OurWays)):
        OurWays[i] = (OurWays[i-1] if i-1 >= 0 else 0) + (OurWays[i-2] if i-2 >= 0 else 0)
    return OurWays[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        self._dict = defaultdict(int)

        def helper(n: int) -> int:
            if n == 0 or n == 1: return 1

            if n in self._dict:
                return self._dict[n]

            self._dict[n] = (x := (helper(n-1) + helper(n-2)))
            return x

        return helper(n)



OurN = 50
X = Solution()
print(X.climbStairs(OurN))
print(climbStairs1(OurN))