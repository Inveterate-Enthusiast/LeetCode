# Given a string s, return the longest palindromic substring in s.

def isPal(s:str) -> bool:
    start = 0
    end = len(s)-1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def longestPalindrome1(s: str) -> str:
    if len(s) < 2:
        return s
    OurLP = s[0]
    for leftIndex in range(len(s)):
        for rightIndex in range(leftIndex+1, len(s)):
            if isPal(s[leftIndex:rightIndex+1]):
                OurLP = OurLP if len(OurLP) >= len(s[leftIndex:rightIndex+1]) else s[leftIndex:rightIndex+1]
    return OurLP


def longestPalindrome2(s: str) -> str:
    if len(s) < 2:
        return s
    OurLP = s[0]
    OurSize = len(s)
    OurTable = [[False] * OurSize for n in range(OurSize)]

    for k in range(OurSize):
        OurTable[k][k] = True

    for i in range(OurSize-1, -1, -1):
        for j in range(i + 1, OurSize):
            if j - i == 1:
                OurTable[i][j] = (s[i] == s[j])
            else:
                OurTable[i][j] = (s[i] == s[j]) and OurTable[i+1][j-1]

            if OurTable[i][j]:
                OurLP = OurLP if len(OurLP) >= len(s[i:j+1]) else s[i:j+1]
    return OurLP


s = "abbba"
print(longestPalindrome2(s))