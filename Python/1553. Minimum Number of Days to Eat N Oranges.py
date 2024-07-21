# There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:
#
# Eat one orange.
# If the number of remaining oranges n is divisible by 2 then you can eat n / 2 oranges.
# If the number of remaining oranges n is divisible by 3 then you can eat 2 * (n / 3) oranges.
# You can only choose one of the actions per day.
#
# Given the integer n, return the minimum number of days to eat n oranges.
from collections import deque

class Solution:
    def minDays1(self, n: int) -> int: # очень медленный вариант
        if not n:
            return 0

        _count = float("inf")
        _queue = deque()
        _queue.append((n, 0))
        while _queue:
            curN, curStep = _queue.popleft()
            if curN == 0:
                _count = _count if _count <= curStep else curStep
                continue

            if not (curN%3): _queue.append((curN - (2 * (curN/3)), curStep+1))
            if not (curN%2): _queue.append((curN - (curN/2), curStep+1))
            _queue.append((curN-1, curStep+1))

        return _count

    def minDays(self, n: int) -> int: # медленный способ
        if not n:
            return 0

        _count = min(
            (1 + self.minDays((n - n/2))) if not (n%2) else (1 + self.minDays(n-1)),
            (1 + self.minDays((n - (2 * (n/3))))) if not (n%3) else (1 + self.minDays(n-1))
        )
        return _count

    def minDays2(self, n: int) -> int: # тоже медленно
        _array = [0] * (n+1)
        for index in range(1, len(_array)):
            x1 = int((index - (2 * (index / 3)))) if not (index%3) else None
            x2 = int((index - (index/2))) if not (index%2) else None
            _array[index] = 1 + min(
                _array[x1] if x1 else float("inf"),
                _array[x2] if x2 else float("inf"),
                _array[index-1]
            )

        return _array[-1]

    def minDays3(self, n: int) -> int: # очень много памяти жрёт
        _dict = {0: 0, 1: 1}
        _stack = deque()
        _stack.append(n)

        while _stack:
            curN = _stack.pop()
            if curN not in _dict:
                _dict[curN] = None
                _stack.append(curN)
                x1 = curN - (2 * (curN / 3))
                x2 = curN - (curN / 2)
                if not (curN%3) and x1 not in _dict: _stack.append(x1)
                if not (curN%2) and x2 not in _dict: _stack.append(x2)
                _stack.append(curN-1)
            else:
                _dict[curN] = 1 + min(
                    _dict.get(curN - (2 * (curN / 3)), float("inf")) if not (curN%3) else float("inf"),
                    _dict.get(curN - (curN / 2), float("inf")) if not (curN%2) else float("inf"),
                    _dict.get(curN - 1, float("inf"))
                )
        return _dict[n]

    def minDays4(self, n: int) -> int:
        _dict = {0: 0, 1: 1}

        def inner(n: int) -> int:
            if n not in _dict:
                _dict[n] = min(n%2 + 1 + inner(n//2), n%3 + 1 + inner(n//3))
            return _dict[n]

        return inner(n)

    def minDays5(self, n: int) -> int:
        _dict = {0: 0, 1: 1}
        _stack = deque()
        _stack.append(n)

        while _stack:
            curN = _stack.pop()
            if curN not in _dict:
                _dict[curN] = None
                _stack.append(curN)
                x1 = curN // 3
                x2 = curN // 2
                if x1 not in _dict: _stack.append(x1)
                if x2 not in _dict: _stack.append(x2)
            else:
                if _dict[curN] is None:
                    _dict[curN] = min(
                        curN % 3 + 1 + _dict[curN//3],
                        curN % 2 + 1 + _dict[curN//2]
                    )
        return _dict[n]


n = 1
X = Solution()
print(X.minDays5(n))