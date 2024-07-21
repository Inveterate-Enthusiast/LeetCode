# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
#
# An interleaving of two strings s and t is a configuration where s and t are divided into n and m
# substrings
#  respectively, such that:
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

def isInterleave1(s1: str, s2: str, s3: str) -> bool:
    if (len(s1) + len(s2)) != len(s3):
        return False

    OurDP = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for rowIndex in range(len(OurDP)):
        for columnIndex in range(len(OurDP[0])):
            if rowIndex == columnIndex == 0:
                OurDP[rowIndex][columnIndex] = True
            elif rowIndex == 0:
                OurDP[rowIndex][columnIndex] = OurDP[rowIndex][columnIndex-1] and s2[columnIndex-1] == s3[columnIndex-1]
            elif columnIndex == 0:
                OurDP[rowIndex][columnIndex] = OurDP[rowIndex-1][columnIndex] and s1[rowIndex-1] == s3[rowIndex-1]
            else:
                OurDP[rowIndex][columnIndex] = (OurDP[rowIndex-1][columnIndex] and s1[rowIndex-1] == s3[rowIndex+columnIndex-1]) or (OurDP[rowIndex][columnIndex-1] and s2[columnIndex-1] == s3[rowIndex+columnIndex-1])

    return OurDP[len(s1)][len(s2)]

s1 = "abcca"; s2 = "dbbca"; s3 = "aadbbcbcac"
print(isInterleave1(s1, s2, s3))