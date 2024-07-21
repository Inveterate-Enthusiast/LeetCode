# A school is trying to take an annual photo of all the students.
# The students are asked to stand in a single file line in non-decreasing order by height.
# Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
#
# You are given an integer array heights representing the current order that the students are standing in.
# Each heights[i] is the height of the ith student in line (0-indexed).
#
# Return the number of indices where heights[i] != expected[i].
from typing import List, Optional
from collections import defaultdict

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_height = sorted(heights, reverse=False)
        ans_count = 0

        for i in range(len(heights)):
            if heights[i] != sort_height[i]:
                ans_count += 1

        return ans_count

    def heightChecker1(self, heights: List[int]) -> int:
        return sum([x1 != x2 for x1, x2 in zip(heights, sorted(heights))])

heights = [1,1,4,2,1,3]
X = Solution()
print(X.heightChecker1(heights))
