# Given a string s consisting of lowercase English letters, return the first letter to appear twice.
#
# Note:
#
# A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
# s will contain at least one letter that appears twice.

from collections import defaultdict

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        our_dict = defaultdict(int)
        for i in s:
            our_dict[i] += 1
            if our_dict[i] == 2:
                return i

        return None

s = "abccbaacz"
x = Solution()
print(x.repeatedCharacter(s))