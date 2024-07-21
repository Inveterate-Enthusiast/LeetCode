# You have a RecentCounter class which counts the number of recent requests within a certain time frame.
#
# Implement the RecentCounter class:
#
# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds,
# and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
# Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
from collections import deque

class RecentCounter1:

    def __init__(self):
        self._list = deque()

    def ping(self, t: int) -> int:
        self._list.append(t)
        leftTime = t; index = (len(self._list)-1)
        count = 0
        while index >= 0 and (t-3000) <= leftTime <= t:
            count += 1
            index -= 1
            leftTime = self._list[index]

        return count

class RecentCounter2:
    def __init__(self):
        self._list = deque()

    def ping(self, t: int) -> int:
        self._list.append(t)

        while self._list[0] < (t-3000):
            self._list.popleft()

        return len(self._list)

class RecentCounter3:
    def __init__(self):
        self.__queue = deque()
    def ping(self, t: int) -> int:
        self.__queue.append(t)
        while not (t-3000) <= self.__queue[0] <= t:
            self.__queue.popleft()
        return len(self.__queue)

X = RecentCounter3()
print(X.ping(1))
print(X.ping(100))
print(X.ping(3001))
print(X.ping(3002))


