# Given an integer n, return the number of structurally unique BST's (binary search trees)
# which has exactly n nodes of unique values from 1 to n.
from typing import Optional, List
from collections import deque

class Solution:
    def numTrees1(self, n: int) -> int:
        OurDist = dict()

        def generate_trees_nums(start: int, end: int) -> int:
            if start >= end:
                return 1
            elif (start, end) in OurDist:
                return OurDist[(start, end)]

            OurCount = 0
            for value in range(start, end+1):
                OurLeftTreesNums = generate_trees_nums(start, value-1)
                OurRightTreesNums = generate_trees_nums(value+1, end)
                OurCount += OurLeftTreesNums * OurRightTreesNums

            OurDist[(start, end)] = OurCount
            return OurCount

        return generate_trees_nums(1, n)

    def numTrees2(self, n: int) -> int:
        if not n:
            return 0

        OurDict = dict()

        def generate_trees_nums(start: int, end: int) -> int:
            if start >= end:
                return 1
            elif (start, end) in OurDict:
                return OurDict[(start, end)]

            OurCount = 0
            for value in range(start, end+1):
                OurLeftTreesNums = generate_trees_nums(start, value-1)
                OurRightTreesNums = generate_trees_nums(value+1, end)
                OurCount += (OurLeftTreesNums * OurRightTreesNums)

            OurDict[(start, end)] = OurCount
            return OurCount

        return generate_trees_nums(1, n)

    def numTrees3(self, n: int) -> int:
        if not n:
            return 0

        OurDict = dict()

        def generate_trees_nums(start:int, end:int) -> int:
            if start >= end:
                return 1
            elif (start, end) in OurDict:
                return OurDict[(start, end)]

            OurCount = 0
            for i in range(start, end+1):
                leftTreeNums = generate_trees_nums(start, i-1)
                rightTreeNums = generate_trees_nums(i+1, end)
                OurCount += (leftTreeNums * rightTreeNums)

            OurDict[(start, end)] = OurCount
            return OurCount

        return generate_trees_nums(1, n)

    def numTrees4(self, n: int) -> int:
        OurDP = {
            0:1,
            1:1,
            2:2
        }
        if n < 3:
            return OurDP[n]

        for i in range(3, n+1):
            num = 0
            for j in range(i):
                num += OurDP[j] * OurDP[i-j-1]
            OurDP[i] = num
        return OurDP[n]

    def numTrees5(self, n: int) -> int:
        OurDict = dict()

        def generate_trees_numbers(start:int, end:int) -> int:
            if start >= end:
                return 1
            elif (start, end) in OurDict:
                return OurDict[(start, end)]

            OurCount = 0
            for rootVal in range(start, end+1):
                leftTreeNums = generate_trees_numbers(start, rootVal-1)
                rightTreeNums = generate_trees_numbers(rootVal+1, end)
                curNums = leftTreeNums * rightTreeNums
                OurCount += curNums

            OurDict[(start, end)] = OurCount
            return OurCount

        return generate_trees_numbers(1, n)

    def numTrees6(self, n: int) -> int:
        OurDPDict = {
            0 : 1,
            1 : 1,
            2 : 2
        }
        if n < 3:
            return OurDPDict[n]

        for length in range(3, n+1):
            nums = 0
            for rootVal in range(length):
                nums += (OurDPDict[rootVal] * OurDPDict[length - rootVal - 1])
            OurDPDict[length] = nums

        return OurDPDict[n]

n = 4
X = Solution()
print(X.numTrees6(n))












