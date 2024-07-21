# Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.
#
# Implement the ZigzagIterator class:
#
# ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
# boolean hasNext() returns true if the iterator still has elements, and false otherwise.
# int next() returns the current element of the iterator and moves the iterator to the next element.
from typing import Optional, List

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self._array = list()
        self._array.extend(v1); self._array.extend(reversed(v2))
        self._index = 0
        print(self._array)

    def next(self) -> int:
        if self.hasNext(): self._index+=1; return self._array[self._index]

    def hasNext(self) -> bool:
        return (self._index+1) < len(self._array)

X = ZigzagIterator([1,2,3], [4,5,6])
print(X.next())
