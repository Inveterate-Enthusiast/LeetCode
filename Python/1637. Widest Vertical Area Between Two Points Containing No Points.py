# Given n points on a 2D plane where points[i] = [xi, yi],
# Return the widest vertical area between two points such that no points are inside the area.
#
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height).
# The widest vertical area is the one with the maximum width.
#
# Note that points on the edge of a vertical area are not considered included in the area.

from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        result = float("-inf")
        for point in range(1, len(points)):
            result = max(result, (points[point][0] - points[point-1][0]))
        return result

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
x = Solution()
print(x.maxWidthOfVerticalArea(points))