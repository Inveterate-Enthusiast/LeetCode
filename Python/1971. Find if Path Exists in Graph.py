# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
# The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
#
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
#
# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

from typing import List
from collections import deque, defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        our_dict = defaultdict(set)
        for i in edges:
            our_dict[i[0]].add(i[1])
            our_dict[i[1]].add(i[0])

        our_set = set()
        our_queue = deque()
        our_queue.append([source])
        while our_queue:
            neighbours = our_queue.popleft()
            for i in neighbours:
                if i == destination:
                    return True
                if not i in our_set:
                    our_queue.append(list(our_dict[i]))
                    our_set.add(i)

        return False

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
x = Solution()
print(x.validPath(n, edges, source, destination))