# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.

from typing import List, Optional

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        curLen = len(s)
        i = 0
        while i < curLen:
            s.insert(i,s.pop())
            i += 1

    def reverseString1(self, s: List[str]) -> None:
        s.reverse()

s = ["h","e","l","l","o"]
X = Solution()
X.reverseString1(s)
print(s)



