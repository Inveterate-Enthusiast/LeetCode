# There is a stream of n (idKey, value) pairs arriving in an arbitrary order,
# where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.
#
# Design a stream that returns the values in increasing order of their IDs by returning
# a chunk (list) of values after each insertion.
# The concatenation of all the chunks should result in a list of the sorted values.
#
# Implement the OrderedStream class:
#
# OrderedStream(int n) Constructs the stream to take n values.
# String[] insert(int idKey, String value) Inserts the pair (idKey, value)
# into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.
from typing import Optional, List

class OrderedStream:

    def __init__(self, n: int):
        self._list = [None] * n
        self._pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self._list[idKey-1] = value
        if (idKey-1) == self._pointer:
            while self._pointer < len(self._list) and self._list[self._pointer]:
                self._pointer += 1
        else:
            return []
        return self._list[idKey-1 : self._pointer]

X = OrderedStream(5)
print(X.insert(3, "ccccc"))
print(X.insert(1,"aaaaa"))
print(X.insert(2, "bbbbb"))
print(X.insert(5,"eeeee"))
print(X.insert(4,"ddddd"))
