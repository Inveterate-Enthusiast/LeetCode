# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
from typing import Optional, Tuple

class MyHashSet1:

    def __init__(self):
        self._list = list()

    def add(self, key: int) -> None:
        left, right = self.__left_bound(self._list, key), self.__right_bound(self._list, key)

        if all(not bool(x) for x in (left, right)):
            self._list.append(key)
        elif (right - left) > 1:
            return
        elif (right - left) == 1:
            self._list.insert(left + 1, key)
        else:
            return

    def remove(self, key: int) -> None:
        left, right = self.__left_bound(self._list, key), self.__right_bound(self._list, key)

        if all(not bool(x) for x in (left, right)):
            return
        elif (right - left) > 1:
            del self._list[left+1]
            return
        elif (right - left) == 1:
            return
        else:
            return

    def contains(self, key: int) -> bool:
        left, right = self.__left_bound(self._list, key), self.__right_bound(self._list, key)

        if all(not bool(x) for x in (left, right)):
            return False
        elif (right - left) > 1:
            return True
        elif (right - left) == 1:
            return False
        else:
            return False

    def __left_bound(self, lst:list, value:int) -> Optional[int]:
        if not lst:
            return None

        left, right = -1, len(lst)
        while (right - left) > 1:
            middle = (left + right) // 2
            if lst[middle] < value:
                left = middle
            else:
                right = middle
        return left

    def __right_bound(self, lst:list, value:int) -> Optional[int]:
        if not lst:
            return None

        left, right = -1, len(lst)
        while (right - left) > 1:
            middle = (right + left) // 2
            if lst[middle] <= value:
                left = middle
            else:
                right = middle
        return right


X = MyHashSet1()
X.add(1)
X.add(2)
X.add(2)
X.add(1)
X.add(3)
print(X.contains(2))
print(X.contains(3))
print(X.contains(4))


