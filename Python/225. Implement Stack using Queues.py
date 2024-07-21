# Implement a last-in-first-out (LIFO) stack using only two queues.
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
#
# Implement the MyStack class:
#
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:
#
# You must use only standard operations of a queue, which means that only push to back,
# peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively.
# You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
from collections import deque

class MyStack:

    def __init__(self):
        self._queue1 = list()
        self._queue2 = list()

    def push(self, x: int) -> None:
        self._queue2 = self._queue1.copy()
        self._queue1.clear()
        self._queue1.append(x)
        self._queue1.extend(self._queue2)

    def pop(self) -> int:
        return self._queue1.pop(0) if self._queue1 else None

    def top(self) -> int:
        return self._queue1[0] if self._queue1 else None

    def empty(self) -> bool:
        return not self._queue1













