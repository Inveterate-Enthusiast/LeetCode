# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
#
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split()
        our_dict = dict()
        our_set = set()
        n = len(pattern)
        if n != len(ss):
            return False

        for i in range(n):
            if not pattern[i] in our_dict:
                if ss[i] in our_set:
                    return False
                else:
                    our_dict[pattern[i]] = ss[i]
                    our_set.add(ss[i])
            else:
                if our_dict[pattern[i]] != ss[i]:
                    return False
        return True

pattern = "abba"
s = "dog dog dog dog"
x = Solution()
print(x.wordPattern(pattern, s))