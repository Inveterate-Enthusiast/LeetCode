# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string
# by deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence1(s: str, t: str) -> bool:
    if len(t) == 0 and len(s) == 0:
        return True
    elif len(s) == 0:
        return True
    elif len(t) == 0:
        return False
    OurNumber = 0
    for char in t:
        if char == s[OurNumber]:
            OurNumber += 1
            if OurNumber > (len(s)-1):
                return True

    return False

def isSubsequence2(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    elif len(s) == 0:
        return True
    index = 0
    for char in t:
        if char == s[index]:
            index += 1
        if index >= len(s):
            return True

    return False

OurS = "a"
OurT = "ahbgdc"
print(isSubsequence2(OurS, OurT))