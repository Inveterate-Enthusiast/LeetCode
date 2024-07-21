# Design a data structure that accepts a stream of integers and checks
# if it has a pair of integers that sum up to a particular value.
#
# Implement the TwoSum class:
#
# TwoSum() Initializes the TwoSum object, with an empty array initially.
# void add(int number) Adds number to the data structure.
# boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
from typing import Optional

class TwoSum1:

    def __init__(self):
        self._numbers = []

    def add(self, number: int) -> None:
        if not self._numbers: self._numbers.append(number); return

        left, right = self.__left_bound(self._numbers, number), self.__right_bound(self._numbers, number)
        if (right - left) == 1:
            self._numbers.insert(right, number)
        else:
            self._numbers.insert(left+1, number)

    def find(self, value: int) -> bool:
        lP, rP = 0, len(self._numbers)-1

        if not self._numbers or len(self._numbers) < 2: return False

        while lP < rP:
            curSum = self._numbers[lP] + self._numbers[rP]
            if curSum == value:
                return True
            elif curSum > value:
                rP -= 1
            elif curSum < value:
                lP += 1
        else:
            if lP >= rP:
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
            middle = (left + right) // 2
            if lst[middle] <= value:
                left = middle
            else:
                right = middle
        return right

class TwoSum2:

    def __init__(self):
        self._numbers = dict()

    def add(self, number: int) -> None:
        self._numbers[number] = self._numbers.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for number in self._numbers:
            if (value - number) in self._numbers:
                if number == (value - number) and self._numbers[number] < 2:
                    continue
                return True
        return False



X = TwoSum1()
X.add(3)
X.add(2)
X.add(1)
print(X.find(2))
print(X.find(3))
print(X.find(4))
print(X.find(5))
print(X.find(6))


