# You are given an array of n strings strs, all of the same length.
#
# The strings can be arranged such that there is one on each line, making a grid.
#
# For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
# abc
# bce
# cae
# You want to delete the columns that are not sorted lexicographically.
# In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted,
# while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
#
# Return the number of columns that you will delete.

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows, cols = len(strs), len(strs[0])
        result = 0
        for col in range(cols):
            prev_letter = None
            for row in range(rows):
                if not prev_letter or prev_letter <= strs[row][col]:
                    prev_letter = strs[row][col]
                else:
                    result += 1
                    break
        return result

strs = ["zyx","wvu","tsr"]
x = Solution()
print(x.minDeletionSize(strs))