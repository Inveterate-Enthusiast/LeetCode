# Given an integer n, return an array ans of length n + 1
# such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

def bit(n:int) -> str:
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n%2) + result
        n = n // 2

    return result

print(bit(0))


def countBits1(n: int) -> list[int]:
    ResultList = [0]
    if not n:
        return ResultList
    for digit in range(1, n+1):
        CountOnes = 0
        while digit > 0:
            CountOnes = CountOnes + 1 if digit%2 == 1 else CountOnes
            digit = digit // 2
        ResultList.append(CountOnes)
    return ResultList

def countBits2(n: int) -> list[int]:
    ResultList = [0]
    if not n:
        return ResultList
    for digit in range(1, n + 1):
        CountOnes = 0
        for char in str(bin(digit)):
            if char == "1":
                CountOnes += 1
        ResultList.append(CountOnes)

    return ResultList

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        result = [None] * (n + 1)
        for i, _ in enumerate(result):
            result[i] = str(bin(i)).count("1")
        
        return result


print(countBits2(2))