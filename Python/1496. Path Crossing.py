# Given a string path, where path[i] = 'N', 'S', 'E' or 'W',
# each representing moving one unit north, south, east, or west, respectively.
# You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
#
# Return true if the path crosses itself at any point, that is,
# if at any time you are on a location you have previously visited. Return false otherwise.


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        _set = set()
        _move = {
            "N": [0, 1],
            "S": [0, -1],
            "E": [1, 0],
            "W": [-1, 0]
        }
        curPlace = (0, 0); _set.add(curPlace)
        for move in path:
            newPlace = tuple(map(lambda x: x[0] + x[1], zip(list(curPlace), _move[move])))
            if newPlace in _set:
                return True
            _set.add((curPlace := newPlace))

        return False



path = "NESWW"
X = Solution()
print(X.isPathCrossing(path))
