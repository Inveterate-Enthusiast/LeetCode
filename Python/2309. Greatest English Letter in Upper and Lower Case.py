# Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s.
# The returned letter should be in uppercase. If no such letter exists, return an empty string.
#
# An English letter b is greater than another letter a if b appears after a in the English alphabet.

class Solution:
    def greatestLetter(self, s: str) -> str:
        s_new = set(s)
        result = str()
        for i in s_new:
            if (i.upper() in s_new) and (i.lower() in s_new):
                result = max(result, i.upper())
        return result

s = "lEeTcOdE"
x = Solution()
print(x.greatestLetter(s))