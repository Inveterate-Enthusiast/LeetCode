# You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi]
# represents an inclusive interval between starti and endi.
#
# Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.
#
# An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges_sort = sorted(ranges, key=lambda x: (x[0], x[1]))
        n = len(ranges)
        index = 0
        for i in range(left, right+1, 1):
            while (index < n) and not((i >= ranges_sort[index][0]) and (i <= ranges_sort[index][1])):
                index += 1
            if index >= n:
                return False

        return True

ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5
x = Solution()
print(x.isCovered(ranges, left, right))