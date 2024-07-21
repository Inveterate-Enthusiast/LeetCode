# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

from typing import List, Optional

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x[0])
        curInt = None
        for i, interval in enumerate(intervals):
            if i == 0:
                curInt = interval[1]
            else:
                if curInt > interval[0]:
                    return False
                curInt = interval[1]

        return True





intervals = [[7,10],[2,4]]
X = Solution()
print(X.canAttendMeetings(intervals))