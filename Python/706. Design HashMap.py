# Design a HashMap without using any built-in hash table libraries.
#
# Implement the MyHashMap class:
#
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap.
# If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
from typing import Optional


class MyHashMap1:

    def __init__(self):
        self._keyList = list()
        self._valueList = list()

    def put(self, key: int, value: int) -> None:
        left, right = self.__left_bound(self._keyList, key), self.__right_bound(self._keyList, key)

        if all(not bool(x) for x in (left, right)):
            self._keyList.append(key)
            self._valueList.append(value)
        elif (right - left) == 1:
            self._keyList.insert(left + 1, key)
            self._valueList.insert(left + 1, value)
        elif (right - left) > 1:
            self._valueList[left + 1] = value
        else:
            pass

    def get(self, key: int) -> int:
        left, right = self.__left_bound(self._keyList, key), self.__right_bound(self._keyList, key)

        if all(not bool(x) for x in (left, right)):
            return -1
        elif (right - left) == 1:
            return -1
        elif (right - left) > 1:
            return self._valueList[left+1]
        else:
            pass

    def remove(self, key: int) -> None:
        left, right = self.__left_bound(self._keyList, key), self.__right_bound(self._keyList, key)

        if all(not bool(x) for x in (left, right)):
            return
        elif (right - left) == 1:
            return
        elif (right - left) > 1:
            del self._keyList[left + 1]
            del self._valueList[left + 1]
        else:
            pass

    def __left_bound(self, lst:list, value:int) -> Optional[int]:
        if not lst:
            return None

        left, right = -1, len(lst)
        while (right - left) > 1:
            middle = (right + left) // 2
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


X = MyHashMap1()
X.put(1,1)
X.put(2,2)
X.put(2,1)





