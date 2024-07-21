# Design and implement a data structure for a compressed string iterator.
# The given compressed string will be in the form of each letter followed by
# a positive integer representing the number of this letter existing in the original uncompressed string.
#
# Implement the StringIterator class:
#
# next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
# hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.
from collections import deque

def encode(string:str) -> list:
    string = string[::-1]
    chars = deque()
    counts = deque()
    while string:
        if string[-1].isalpha():
            chars.append(string.pop())
        else:
            num = 0
            while string and string[-1].isdigit():
                num = 10 * num + int(s.pop())
            counts.append(num)
    return list(zip(chars, counts))[::-1]





class StringIterator1:

    def __init__(self, compressedString: str):
        self._queue = deque()
        digitStr = ""
        for i in range(len(compressedString)):
            if compressedString[i].isalpha():
                if self._queue:
                    self._queue[-1][1] = int(digitStr)
                    digitStr = ""
                char = compressedString[i]
                self._queue.append([char, 0])
            else:
                digitStr += compressedString[i]
        else:
            self._queue[-1][1] = int(digitStr)

    def next(self) -> str:
        if not self._queue:
            return " "
        char = self._queue[0][0]
        if self._queue[0][1] <= 1:
            self._queue.popleft()
        else:
            self._queue[0][1] -= 1
        return char

    def hasNext(self) -> bool:
        return not not self._queue

class StringIterator2:

    def __init__(self, compressedString: str):
        self._stack = deque(reversed(self.encode(compressedString)))

    def next(self) -> str:
        if not self.hasNext(): return " "
        char, count = self._stack.pop()
        if count > 1:
            count -= 1
            self._stack.append((char, count))
        return char


    def hasNext(self) -> bool:
        return bool(self._stack)

    def encode(self, string: str) -> list:
        string = list(string[::-1])
        chars = []
        digits = []

        while string:
            if string[-1].isalpha():
                chars.append(string.pop())
            else:
                curNum = 0
                while string and string[-1].isdigit():
                    curNum = 10 * curNum + int(string.pop())
                digits.append(curNum)

        return list(zip(chars, digits))


X = StringIterator2("x6")
print(X.next())
print(X.next())
print(X.next())
print(X.next())
print(X.next())

