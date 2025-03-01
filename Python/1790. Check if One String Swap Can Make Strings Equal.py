# You are given two strings s1 and s2 of equal length.
# A string swap is an operation where you choose two indices in a string (not necessarily different)
# and swap the characters at these indices.
#
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings.
# Otherwise, return false.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dif_1, dif_2 = (-1), (-1)

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if dif_1 == (-1):
                    dif_1 = i
                elif dif_2 == (-1):
                    dif_2 = i
                else:
                    return False
        return s1[dif_1] == s2[dif_2] and s1[dif_2] == s2[dif_1]

s1 = "bankb"
s2 = "kannb"
x = Solution()
print(x.areAlmostEqual(s1, s2))