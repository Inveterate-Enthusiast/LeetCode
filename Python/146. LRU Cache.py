# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
# evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self._dict_storage = dict()
        self._capacity = capacity

    def get(self, key: int) -> int:
        if key in self._dict_storage:
            value = self._dict_storage[key]
            del self._dict_storage[key]
            self._dict_storage[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._dict_storage:
            del self._dict_storage[key]
        elif key not in self._dict_storage and len(self._dict_storage) == self._capacity:
            for k, v in self._dict_storage.items():
                del self._dict_storage[k]
                break
        self._dict_storage[key] = value



