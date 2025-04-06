# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase.
# For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.
#
# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring
# of the earliest occurrence. If there are none, return an empty string.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        result = str()
        for i in range(len(s)):
            past, wait = set(), set()
            for j in range(i, len(s)):
                if s[j].swapcase() in past:
                    past.add(s[j])
                elif s[j].swapcase() in wait:
                    past.add(s[j])
                    past.add(s[j].swapcase())
                    wait.remove(s[j].swapcase())
                else:
                    wait.add(s[j])
                if not len(wait):
                    result = result if len(result) >= len(s[i:j+1]) else s[i:j+1]
        return result

s = "YazaAay"
x = Solution()
print(x.longestNiceSubstring(s))