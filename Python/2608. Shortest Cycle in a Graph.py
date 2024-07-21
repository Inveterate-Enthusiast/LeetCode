# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1.
# The edges in the graph are represented by a given 2D integer array edges, where edges[i] = [ui, vi]
# denotes an edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
#
# Return the length of the shortest cycle in the graph. If no cycle exists, return -1.
#
# A cycle is a path that starts and ends at the same node, and each edge in the path is used only once.

from typing import List, Optional
from collections import deque

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int: # неправильное решение
        AdjList = {i: [set(), None, False, 0] for i in range(n)} # value is list of set of vertex's neighbours, its parent, visited flag and its distance
        ansMinCycle = (-1)
        for edge in edges:
            u, v = edge
            AdjList[u][0].add(v); AdjList[v][0].add(u)

        _queue = deque()
        for vertex in AdjList:
            if not AdjList[vertex][2]:
                AdjList[vertex][2] = True
                _queue.append(vertex)
                while _queue:
                    curVertex = _queue.popleft()
                    for neighbour in AdjList[curVertex][0]:
                        if not AdjList[neighbour][2]:
                            AdjList[neighbour][2] = True
                            AdjList[neighbour][3] = AdjList[curVertex][3] + 1
                            AdjList[neighbour][1] = curVertex
                            _queue.append(neighbour)
                        elif AdjList[curVertex][1] != neighbour:
                            commonParent, parent1, parent2 = None, curVertex, neighbour
                            while commonParent is None:
                                if parent1 == parent2:
                                    commonParent = parent1
                                elif AdjList[parent1][3] >= AdjList[parent2][3]:
                                    parent1 = AdjList[parent1][1]
                                else:
                                    parent2 = AdjList[parent2][1]

                            curDistance = (AdjList[curVertex][3] + AdjList[neighbour][3] + 1 - (2*AdjList[commonParent][3]))
                            ansMinCycle = curDistance if ansMinCycle == (-1) else min(ansMinCycle, curDistance)
            else:
                AdjList[vertex][1] = set()

        return ansMinCycle

    def findShortestCycle1(self, n: int, edges: List[List[int]]) -> int:
        AdjList = {i: set() for i in range(n)}
        for edge in edges:
            v, u = edge
            AdjList[v].add(u); AdjList[u].add(v)

        def nearestCycle(startVertex: int) -> Optional[int]:
            _queue = deque()
            _distance_dict = dict()
            _queue.append((startVertex, None)) # vertex and its parent
            _distance_dict[startVertex] = 0
            _shortest_distance = float("inf")
            while _queue:
                tempVertex, tempParent = _queue.popleft()
                for neighbour in AdjList[tempVertex]:
                    if neighbour not in _distance_dict:
                        _distance_dict[neighbour] = _distance_dict[tempVertex] + 1
                        _queue.append((neighbour, tempVertex))
                    elif neighbour != tempParent:
                        _shortest_distance = min(_shortest_distance, (_distance_dict[neighbour] + _distance_dict[tempVertex] + 1))
            return _shortest_distance

        ansMinCycle = float("inf")
        for vertex in AdjList:
            curDistance = nearestCycle(vertex)
            ansMinCycle = min(ansMinCycle, curDistance)

        return ansMinCycle if ansMinCycle != float("inf") else (-1)

n = 8; edges = [[7,3],[1,5],[0,6],[3,1],[6,2],[7,4],[3,2],[5,2],[6,5],[0,3]]
X = Solution()
print(X.findShortestCycle1(n, edges))
