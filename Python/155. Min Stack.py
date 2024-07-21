# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self._dict_stack = dict()

    def push(self, val: int) -> None:
        if not self._dict_stack:
            self._dict_stack[0] = (val, val)
        else:
            pastKey, pastTuple = self.__get_past()
            pastValue, pastMin = pastTuple
            pastMin = min(pastMin, val)
            self._dict_stack[pastKey+1] = (val, pastMin)

    def pop(self) -> None:
        pastKey, pastTuple = self.__get_past()
        del self._dict_stack[pastKey]

    def top(self) -> int:
        pastKey, pastTuple = self.__get_past()
        return pastTuple[0]

    def getMin(self) -> int:
        pastKey, pastTuple = self.__get_past()
        return pastTuple[1]

    def __get_past(self):
        return next(reversed(self._dict_stack.items()))

X = MinStack()
X.push(-2)
X.push(0)
X.push(-3)
print(X.getMin())
X.pop()
print(X.top())
print(X.getMin())




