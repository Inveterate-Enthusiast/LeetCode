# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        our_dict = {(i - 65 + 1): chr(i) for i in range(65, 91)}
        temp = columnNumber
        result = str()
        while temp > 0:
            char = temp % 26
            if char:
                result = our_dict[char] + result
                temp = temp // 26
            else:
                result = our_dict[26] + result
                temp = temp // 26 - 1

        return result


columnNumber = 28
x = Solution()
print(x.convertToTitle(columnNumber))