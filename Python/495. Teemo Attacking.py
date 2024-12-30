# Our hero Teemo is attacking an enemy Ashe with poison attacks!
# When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds.
# More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1].
# If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will
# end duration seconds after the new attack.
#
# You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i],
# and an integer duration.
#
# Return the total number of seconds that Ashe is poisoned.
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        prev = None
        result = 0
        for time in timeSeries:
            if not prev is None:
                if (time - prev) >= duration:
                    result += duration
                elif time != prev:
                    result += (time - prev)
            prev = time
        else:
            result += duration
        return result

timeSeries = [0,1,2,3,4,5]; duration = 1
x = Solution()
print(x.findPoisonedDuration(timeSeries, duration))