# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
# The lengths should not have leading zeros.
#
# For example, a string such as "substitution" could be abbreviated as (but not limited to):
#
# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:
#
# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
#
# A substring is a contiguous non-empty sequence of characters within a string.


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not word and not abbr:
            return True
        elif not word or not abbr:
            return False

        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if word[i] == abbr[j]: i += 1; j += 1
                else: return False
            else:
                if abbr[j] == "0": return False
                jj = j
                while j < len(abbr) and abbr[j].isdigit(): j += 1
                i += int(abbr[jj:j])
        return i == len(word) and j == len(abbr)







word = "aa"; abbr = "a1"
X = Solution()
print(X.validWordAbbreviation(word, abbr))
