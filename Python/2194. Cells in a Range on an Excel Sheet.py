# A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:
#
# <col> denotes the column number c of the cell. It is represented by alphabetical letters.
# For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
# <row> is the row number r of the cell. The rth row is represented by the integer r.
# You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the column c1,
# <row1> represents the row r1, <col2> represents the column c2, and <row2> represents the row r2,
# such that r1 <= r2 and c1 <= c2.
#
# Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2.
# The cells should be represented as strings in the format mentioned above
# and be sorted in non-decreasing order first by columns and then by rows.

from typing import List
import re

class Solution:
    def col_to_num(self, col):
        num = 0
        for char in col:
            num = num * 26 + (ord(char.upper()) - ord("A") + 1)
        return num

    def num_to_col(self, num):
        col = str()
        while num > 0:
            num, rem = divmod(num - 1, 26)
            col = chr(65 + rem) + col
        return col

    def col_range(self, col_start, col_end):
        num_start = self.col_to_num(col_start)
        num_end = self.col_to_num(col_end)
        return [self.num_to_col(i) for i in range(num_start, num_end + 1)]

    def cellsInRange(self, s: str) -> List[str]:
        letter_start, letter_end = re.match(r"^(\w+)\d+:.*$", s).groups()[0], re.match(r"^.*:(\w+)\d+$", s).groups()[0]
        digit_start, digit_end = int(re.match(r"^\w+(\d+):.*$", s).groups()[0]), int(re.match(r".*:\w+(\d+)", s).groups()[0])

        result = list()
        for letter in self.col_range(letter_start, letter_end):
            for digit in range(digit_start, digit_end + 1):
                result.append(letter + str(digit))

        return result


s = "K1:LL2"
x = Solution()
print(x.cellsInRange(s))