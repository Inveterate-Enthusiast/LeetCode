# There are n piles of stones arranged in a row. The ith pile has stones[i] stones.
#
# A move consists of merging exactly k consecutive piles into one pile,
# and the cost of this move is equal to the total number of stones in these k piles.
#
# Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.
from typing import List, Optional
from collections import deque

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int: # медленное и неправильное
        if not stones:
            return -1
        elif len(stones) == 1:
            return 0

        _queue = deque()
        _queue.append((stones, 0))
        minCost = float("inf")
        while _queue:
            curPiles, curCost = _queue.popleft()
            curLen = len(curPiles)
            if curLen == k:
                minCost = min(minCost, (curCost + sum(curPiles)))
                continue

            i = 0
            while (i+k-1) < curLen:
                left = curPiles[:i]
                right = curPiles[i+k:]
                newPile = sum(curPiles[i:i+k])
                _queue.append((left + [newPile] + right, curCost+newPile))
                i += 1

        minCost = minCost if minCost != float("inf") else (-1)
        return minCost

    def mergeStones1(self, stones: List[int], k: int) -> int: # неправильное
        if not stones:
            return -1
        elif len(stones) == 1:
            return 0

        curPiles = stones; curCost = 0
        while True:
            curLen = len(curPiles)
            if curLen == k:
                curCost += sum(curPiles)
                break
            elif curLen < k:
                return -1

            _min = float("inf")
            i = 0
            _dict = dict()
            while (i+k-1) < curLen:
                left = curPiles[:i]
                newPile = sum(curPiles[i:i+k])
                right = curPiles[i+k:]
                newStones = left + [newPile] + right
                _min = min(_min, newPile)
                _dict[newPile] = newStones
                i += 1

            curPiles = _dict[_min]
            curCost += _min

        return curCost

    def mergeStones2(self, stones: List[int], k: int) -> int:
        stoneLen = len(stones)

        if (stoneLen - 1) % (k - 1):
            return (-1)

        prefSum = [0] * (stoneLen + 1)
        for i, _ in enumerate(prefSum):
            if i < stoneLen: prefSum[i + 1] = prefSum[i] + stones[i]

        OurDP = [[0] * stoneLen for _ in range(stoneLen)]

        for size in range(k, stoneLen + 1):
            for i in range(stoneLen - size + 1):
                j = i + size - 1
                if size > k:
                    OurDP[i][j] = min([OurDP[i][t] + OurDP[t + 1][j] for t in range(i, j, k - 1)])
                if (size - 1) % (k - 1) == 0:
                    OurDP[i][j] += prefSum[j + 1] - prefSum[i]

        return OurDP[0][stoneLen - 1]




stones = [6,4,4,6]; k = 2
X = Solution()
print(X.mergeStones2(stones, k))







