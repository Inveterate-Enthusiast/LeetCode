# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False

        our_dict = dict()
        our_set = set()

        for i in range(n):
            if not s[i] in our_dict:
                if t[i] in our_set:
                    return False
                else:
                    our_dict[s[i]] = t[i]
                    our_set.add(t[i])
            else:
                if our_dict[s[i]] != t[i]:
                    return False
        return True


s = "badc"
t = "baba"
x = Solution()
print(x.isIsomorphic(s, t))