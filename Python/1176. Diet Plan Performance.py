# A dieter consumes calories[i] calories on the i-th day.
#
# Given an integer k, for every consecutive sequence of k days
# (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k),
# they look at T, the total calories consumed during
# that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):
#
# If T < lower, they performed poorly on their diet and lose 1 point;
# If T > upper, they performed well on their diet and gain 1 point;
# Otherwise, they performed normally and there is no change in points.
# Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for calories.length days.
#
# Note that the total points can be negative.

def dietPlanPerformance(calories: list[int], k: int, lower: int, upper: int) -> int:
    pastDay = endDay = 0
    OurResultPoints = 0
    OurCurrentColiries = 0
    for endDay in range(len(calories)):
        OurCurrentColiries += calories[endDay]
        if (endDay - pastDay + 1) < k:
            continue
        while pastDay <= endDay and (endDay - pastDay + 1) > k:
            OurCurrentColiries -= calories[pastDay]
            pastDay += 1
        if (endDay - pastDay + 1) == k:
            if OurCurrentColiries < lower:
                OurResultPoints -= 1
            elif OurCurrentColiries > upper:
                OurResultPoints += 1
    return OurResultPoints

calories = [3,2]; k = 2; lower = 0; upper = 1
print(dietPlanPerformance(calories, k, lower, upper))
