# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def isAnagram1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    SDict = {}
    TDict = {}
    for char in s:
        SDict[char] = SDict.get(char, 0) + 1
    for char in t:
        TDict[char] = TDict.get(char, 0) + 1
    for char in SDict:
        if char not in TDict or SDict[char] != TDict[char]:
            return False
    return True

s = "rat"; t = "car"
print(isAnagram1(s, t))