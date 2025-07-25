# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
#
# A shift on s consists of moving the leftmost character of s to the rightmost position.
#
# For example, if s = "abcde", then it will be "bcdea" after one shift.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(goal)
        if len(s) != n:
            return False
        if n == 1:
            return s == goal

        ss = s + s
        prev = [0] * n
        i, j = 1, 0
        while i < n:
            if goal[j] == goal[i]:
                prev[i] = j + 1
                i += 1; j += 1
            else:
                if j == 0:
                    prev[i] = 0
                    i += 1
                else:
                    j = prev[j - 1]

        i = j = 0
        while i < (n * 2):
            if ss[i] == goal[j]:
                if j == (n - 1):
                    return True
                i += 1; j += 1
            else:
                if j > 0:
                    j = prev[j - 1]
                else:
                    i += 1
        return False

s = "defdefdefabcabc"
goal = "defdefabcabcdef"
x = Solution()
print(x.rotateString(s, goal))