# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.

def minCostClimbingStairs1(cost: list[int]) -> int:
    OurWays = [0] * (len(cost) + 2)
    for indexStep in range(1, len(OurWays)):
        OurMin = min((OurWays[indexStep-1] if (indexStep-1) >= 0 else float("inf")), (OurWays[indexStep-2] if (indexStep-2) >= 0 else float("inf")))
        OurWays[indexStep] = OurMin + (cost[indexStep-1] if indexStep-1 < len(cost) else 0)
    return OurWays[-1]

cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs1(cost))