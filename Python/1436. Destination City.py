# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
# Return the destination city, that is, the city without any path outgoing to another city.
#
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        our_set = set()
        dest_set = set()
        for path in paths:
            if path[0] in dest_set:
                dest_set.remove(path[0])

            if not path[1] in our_set:
                dest_set.add(path[1])

            our_set.add(path[0])

        return list(dest_set)[0] if dest_set else None

paths = [["B","C"],["D","B"],["C","A"]]
x = Solution()
print(x.destCity(paths))