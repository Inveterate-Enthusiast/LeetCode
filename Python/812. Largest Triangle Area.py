# Given an array of points on the X-Y plane points where points[i] = [xi, yi],
# return the area of the largest triangle that can be formed by any three different points.
# Answers within 10-5 of the actual answer will be accepted.

from typing import List
import itertools

class Solution:
    def length(self, a, b) -> float:
        return ((b[0] - a[0])**2 + (b[1] - a[1])**2)**(1/2)

    def square(self, a, b, c) -> float:
        p1, p2, p3 = self.length(a, b), self.length(b, c), self.length(c, a)
        p = (p1 + p2 + p3) / 2
        s = (p * (p - p1) * (p - p2) * (p - p3))
        return 0 if s <= 0 else s**(1/2)

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        result = 0
        for a, b, c in itertools.combinations(points, 3):
            result = max(result, self.square(a, b, c))
        return result

points = [[-35,19],[40,19],[27,-20],[35,-3],[44,20],[22,-21],[35,33],[-19,42],[11,47],[11,37]]
x = Solution()
print(x.largestTriangleArea(points))