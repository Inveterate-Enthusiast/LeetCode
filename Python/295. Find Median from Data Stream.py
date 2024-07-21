# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
# and the median is the mean of the two middle values.
#
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
from typing import Optional
from math import floor, ceil
class MedianFinder:

    def __init__(self):
        self._list = list()

    def addNum(self, num: int) -> None:
        if not self._list:
            self._list.append(num)
        else:
            self._list.insert((self.__get_left(num)) + 1, num)


    def findMedian(self) -> float:
        cur_len = len(self._list)
        if cur_len % 2:
            return self._list[cur_len // 2]
        else:
            left, right = int(cur_len / 2 - 1), int(cur_len / 2)
            return (self._list[left] + self._list[right]) / 2

    def __get_left(self, num: int) -> Optional[int]:
        if not self._list: return None

        left, right = -1, len(self._list)
        while (right - left) > 1:
            middle = (right + left) // 2
            if self._list[middle] < num:
                left = middle
            else:
                right = middle
        return left

X = MedianFinder()
X.addNum(1)
X.addNum(2)
print(X.findMedian())
X.addNum(3)
print(X.findMedian())




