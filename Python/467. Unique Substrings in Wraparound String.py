# We define the string base to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz",
# so base will look like this:
#
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# Given a string s, return the number of unique non-empty substrings of s are present in base.

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        OurAnswer = Count = 0
        PassedDict = dict()
        for i in range(len(s)):
            if 0 < i and (ord(s[i]) - ord(s[i-1])) % 26 != 1:
                Count = 0

            Count += 1
            x = PassedDict.get(s[i], 0)
            if Count > x:
                OurAnswer += (Count - x)
                PassedDict[s[i]] = Count
        return OurAnswer
