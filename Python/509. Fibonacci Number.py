# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

def fib1(n: int) -> int:
    if n <= 1:
        return n
    OurFibList = [0, 1]
    for i in range(2, n+1):
        OurFibList.append(((OurFibList[i-1]) if (i-1) >= 0 else 0) + ((OurFibList[i-2]) if (i-2) >= 0 else 0))
    return OurFibList[-1]

print(fib1(4))