# You are given an array of non-overlapping intervals intervals
# where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order
# by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

def insert1(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    if len(newInterval) == 0:
        return intervals
    elif len(intervals) == 0:
        if len(newInterval) > 0:
            return [newInterval]
        else:
            return intervals
    elif len(intervals) == 1:
        if intervals[0][1] < newInterval[0]:
            intervals.append(newInterval)
        elif intervals[0][0] > newInterval[1]:
            intervals = [newInterval,intervals[0]]
        else:
            intervals[0][0] = newInterval[0] if newInterval[0] < intervals[0][0] else intervals[0][0]
            intervals[0][1] = newInterval[1] if newInterval[1] > intervals[0][1] else intervals[0][1]
        return intervals

    OurResultInterval = []
    OurFlag = False
    for index in range(len(intervals)):
        if intervals[index][1] < newInterval[0]:
            OurResultInterval.append(intervals[index])
        elif intervals[index][0] > newInterval[1]:
            if not OurFlag:
                OurResultInterval.append(newInterval)
                OurFlag = True
            OurResultInterval.append(intervals[index])
        else:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
    if not OurFlag:
        OurResultInterval.append(newInterval)
    return OurResultInterval

OurIntervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
OurNewInterval = [17,18]

print(insert1(OurIntervals, OurNewInterval))