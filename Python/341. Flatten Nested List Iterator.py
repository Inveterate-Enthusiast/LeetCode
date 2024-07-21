# You are given a nested list of integers nestedList. Each element is either an integer
# or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
#
# Implement the NestedIterator class:
#
# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# Your code will be tested with the following pseudocode:
#
# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res
# If res matches the expected flattened list, then your code will be judged as correct.
from typing import List, Optional, Tuple
from collections import deque, defaultdict


class NestedIterator:
    _queue = deque()

    def __init__(self, nestedList: [NestedInteger]):
        for _object in nestedList:
            if _object.isInteger():
                self._queue.append(_object.getInteger())
            else:
                self.__init__(_object.getList())

    def next(self) -> int:
        return self._queue.popleft()

    def hasNext(self) -> bool:
        return bool(self._queue)

class NestedIterator1:
    def __init__(self, nestedList: [NestedInteger]):
        self._queue = deque()
        self.__flatten(nestedList)

    def __flatten(self, nestedList: [NestedInteger]):
        for obj in nestedList:
            if obj.isInteger():
                self._queue.append(obj.getInteger())
            else:
                self.__flatten(obj.getList())

    def next(self) -> int:
        return self._queue.popleft()

    def hasNext(self) -> bool:
        return bool(self._queue)