# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss, tt = list(), list()
        for char in s:
            if char == "#":
                if ss: ss.pop()
            else:
                ss.append(char)

        for char in t:
            if char == "#":
                if tt: tt.pop()
            else:
                tt.append(char)

        return ss == tt

s = "y#fo##f"
t = "y#f#o##f"
x = Solution()
print(x.backspaceCompare(s, t))