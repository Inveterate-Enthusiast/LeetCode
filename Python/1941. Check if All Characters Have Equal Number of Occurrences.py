# Given a string s, return true if s is a good string, or false otherwise.
#
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        our_dict = defaultdict(int)
        for i in s:
            our_dict[i] += 1

        prev = our_dict[s[0]]
        for key, value in our_dict.items():
            if value != prev:
                return False
            prev = value

        return True

s = "abacbc"
x = Solution()
print(x.areOccurrencesEqual(s))