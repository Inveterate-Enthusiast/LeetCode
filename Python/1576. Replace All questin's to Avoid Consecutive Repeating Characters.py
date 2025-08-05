# Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters
# into lowercase letters such that the final string does not contain any consecutive repeating characters.
# You cannot modify the non '?' characters.
#
# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
#
# Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution,
# return any of them. It can be shown that an answer is always possible with the given constraints.

class Solution:
    def modifyString(self, s: str) -> str:
        chars = [chr(i) for i in range(97, 122+1)]
        result = str()
        n = len(s)
        for i in range(n):
            if s[i].isalpha():
                result += s[i]
                continue

            prev = (result[i - 1] if result[i - 1].isalpha() else None) if i > 0 else None
            next = (s[i + 1] if s[i + 1].isalpha() else None) if i < (n - 1) else None
            j = 0
            while (False if not prev else chars[j] == prev) or (False if not next else chars[j] == next):
                j += 1
            result += chars[j]

        return result

s = "?zs"
x = Solution()
print(x.modifyString(s))