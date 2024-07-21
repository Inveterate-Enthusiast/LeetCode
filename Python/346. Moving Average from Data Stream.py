# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Implement the MovingAverage class:
#
# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self._queue = deque(maxlen=size)
        self._curSum = 0

    def __append_return(self, element: int) -> int:
        self._queue.append(element)
        return element

    def next(self, val: int) -> float:
        if len(self._queue) == self._queue.maxlen:
            self._curSum += (-(self._queue.popleft()) + (self.__append_return(val)))
        else:
            self._curSum += self.__append_return(val)

        return self._curSum / len(self._queue)

MyQueue = deque(maxlen=3)
MyQueue.append(2)
MyQueue.append(5)
MyQueue.append(6)
print(MyQueue.append(4))
print(len(MyQueue))
print(MyQueue)


