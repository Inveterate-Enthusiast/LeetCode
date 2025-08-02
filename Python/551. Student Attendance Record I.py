# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent,
# late, or present on that day. The record only contains the following three characters:
#
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
#
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.

class Solution:
    def checkRecord(self, s: str) -> bool:
        A, L = 0, 0
        for char in s:
            if char == "A":
                A += 1
                if A >= 2:
                    return False

            if char == "L":
                L += 1
                if L >= 3:
                    return False
            else:
                L = 0

        return True

s = "LALL"
x = Solution()
print(x.checkRecord(s))