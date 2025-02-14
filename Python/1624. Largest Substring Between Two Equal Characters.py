# Given a string s, return the length of the longest substring between two equal characters,
# excluding the two characters. If there is no such substring return -1.
#
# A substring is a contiguous sequence of characters within a string.

from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        our_dict = defaultdict(int)
        result = -1
        for index, char in enumerate(s):
            if char in our_dict:
                result = max(result, index - our_dict[char] + 1 - 2)
            else:
                our_dict[char] = index

        return result

s = "cbzxy"
x = Solution()
print(x.maxLengthBetweenEqualCharacters(s))