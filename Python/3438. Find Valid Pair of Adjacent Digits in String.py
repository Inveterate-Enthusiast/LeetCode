# You are given a string s consisting only of digits. A valid pair is defined as two adjacent digits in s such that:
#
# The first digit is not equal to the second.
# Each digit in the pair appears in s exactly as many times as its numeric value.
# Return the first valid pair found in the string s when traversing from left to right. If no valid pair exists, return an empty string.

from collections import defaultdict

class Solution:
    def findValidPair(self, s: str) -> str:
        our_dict = defaultdict(int)
        for i in s:
            our_dict[i] += 1

        for i in range(1, len(s)):
            if (s[i - 1] != s[i]) and (int(s[i - 1]) == our_dict[s[i - 1]]) and (int(s[i]) == our_dict[s[i]]):
                return s[(i - 1):(i + 1)]

        return str()

s = "2523533"
x = Solution()
print(x.findValidPair(s))