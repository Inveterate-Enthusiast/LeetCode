# Given an integer num, return a string of its base 7 representation.

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"

        result, nnum = str(), abs(num)
        while nnum:
            temp = nnum % 7
            result = str(temp) + result
            nnum = nnum // 7

        return result if num > 0 else ("-" + result)

num = (-7)
x = Solution()
print(x.convertToBase7(num))