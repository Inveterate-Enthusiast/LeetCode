# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.

from collections import defaultdict
from typing import List, Optional

def minCostClimbingStairs1(cost: list[int]) -> int:
    OurWays = [0] * (len(cost) + 2)
    for indexStep in range(1, len(OurWays)):
        OurMin = min((OurWays[indexStep-1] if (indexStep-1) >= 0 else float("inf")), (OurWays[indexStep-2] if (indexStep-2) >= 0 else float("inf")))
        OurWays[indexStep] = OurMin + (cost[indexStep-1] if indexStep-1 < len(cost) else 0)
    return OurWays[-1]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self._dict = defaultdict(int)
        self._dict[0] = 0; self._dict[1] = cost[0]

        def helper(stair:int):
            if stair in self._dict:
                return self._dict[stair]
            
            self._dict[stair] = min(helper(stair-1), helper(stair-2)) + cost[stair-1]
            return self._dict[stair]

        helper(len(cost))

        return min(self._dict[len(cost)], self._dict[len(cost)-1])


cost = [1,100,1,1,1,100,1,1,100,1]
X = Solution()
print(X.minCostClimbingStairs(cost))