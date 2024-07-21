# Suppose we have a class:
#
# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
# The same instance of Foo will be passed to three different threads.
# Thread A will call first(), thread B will call second(), and thread C will call third().
# Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().
#
# Note:
#
# We do not know how the threads will be scheduled in the operating system,
# even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.
import asyncio
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Lock, Value
import time
from threading import Thread, Condition

class Foo:
    def __init__(self):
        self._lock = Condition()
        self._counter = Value("i", 1)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        with self._lock:
            while self._counter.value != 1:
                self._lock.wait()
            printFirst()
            self._counter.value += 1
            self._lock.notify_all()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self._lock:
            while self._counter.value != 2:
                self._lock.wait()
            printSecond()
            self._counter.value += 1
            self._lock.notify_all()


    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self._lock:
            while self._counter.value != 3:
                self._lock.wait()
            printThird()
            self._counter.value += 1
            self._lock.notify_all()

if __name__ == "__main__":
    foo = Foo()
    Thread(target=Foo.second, args=(foo, lambda:print(2), )).start()
    Thread(target=Foo.first, args=(foo, lambda:print(1), )).start()
    Thread(target=Foo.third, args=(foo, lambda:print(3), )).start()

