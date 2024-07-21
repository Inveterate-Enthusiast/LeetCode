# Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.
#
# Implement the Vector2D class:
#
# Vector2D(int[][] vec) initializes the object with the 2D vector vec.
# next() returns the next element from the 2D vector and moves the pointer one step forward.
# You may assume that all the calls to next are valid.
# hasNext() returns true if there are still some elements in the vector, and false otherwise.


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self._dict = dict()
        self._index = index = 0
        for i in vec:
            for j in i:
                self._dict[index] = j
                index += 1

    def next(self) -> int:
        if not self.hasNext():
            return None
        ans = self._dict[self._index]
        del self._dict[self._index]; self._index += 1
        return ans

    def hasNext(self) -> bool:
        return bool(self._dict)


