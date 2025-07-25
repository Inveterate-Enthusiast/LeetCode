# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str: # runtime error
        return str(int(num1) + int(num2))

    def addStrings1(self, num1: str, num2: str) -> str:
        num_1 = 0
        for num in num1:
            num_1 = num_1 * 10 + int(num)

        num_2 = 0
        for num in num2:
            num_2 = num_2 * 10 + int(num)


        num_3 = num_1 + num_2
        if num_3 == 0:
            return str(num_3)
        result = str()
        while num_3 > 0:
            temp = num_3 % 10
            result = str(temp) + result
            num_3 = num_3 // 10
        return result

num1 = "0"
num2 = "0"
x = Solution()
print(x.addStrings1(num1, num2))