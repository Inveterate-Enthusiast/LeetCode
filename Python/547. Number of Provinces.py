# There are n cities. Some of them are connected, while some are not.
# If city a is connected directly with city b, and city b is connected directly with city c,
# then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
# and isConnected[i][j] = 0 otherwise.
#
# Return the total number of provinces.
from typing import List
from collections import defaultdict as ddict, deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        OurProvince = ddict(set)
        OurCities = {i: set() for i in range(len(isConnected))}
        passedCitites = set()

        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1:
                    OurCities[i].add(j)
                    OurCities[j].add(i)

        newProvince = 0
        _queue = deque()
        for city in OurCities:
            if city in passedCitites:
                continue
            OurProvince[(newProvince := newProvince + 1)].add(city)
            _queue.extend(list(OurCities[city]))
            passedCitites.add(city)
            while _queue:
                neighbour = _queue.popleft()
                OurProvince[newProvince].add(neighbour)
                passedCitites.add(neighbour)
                for x in OurCities[neighbour]:
                    if x not in passedCitites:
                        _queue.append(x)

        return len(OurProvince)

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        matrixLen = len(isConnected)
        visitFlags = [False] * matrixLen
        OurProvince = ddict(set)
        OurCities = ddict(int)
        newProvince = 0
        OurQueue = deque()

        for i in range(matrixLen):
            if not visitFlags[i]:
                visitFlags[i] = True
                OurProvince[(newProvince := newProvince + 1)].add(i)
                OurCities[i] = newProvince
                OurQueue.append(i)
                while OurQueue:
                    curCity = OurQueue.popleft()
                    OurProvince[newProvince].add(curCity)
                    OurCities[curCity] = newProvince
                    for j in range(matrixLen):
                        if not visitFlags[j] and isConnected[curCity][j]:
                            visitFlags[j] = True
                            OurQueue.append(j)
        return len(OurProvince)

    def findCircleNum3(self, isConnected: List[List[int]]) -> int:
        matrixLen = len(isConnected)
        visitFlags = [False] * matrixLen
        Provinces_count = 0
        OurQueue = deque()

        for i in range(matrixLen):
            if not visitFlags[i]:
                visitFlags[i] = True
                OurQueue.append(i)
                while OurQueue:
                    curCity = OurQueue.popleft()
                    for j in range(matrixLen):
                        if not visitFlags[j] and isConnected[curCity][j]:
                            visitFlags[j] = True
                            OurQueue.append(j)
                Provinces_count += 1
        return Provinces_count

isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
X = Solution()
print(X.findCircleNum3(isConnected))