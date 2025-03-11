# A string is good if there are no repeated characters.
#
# Given a string s, return the number of good substrings of length three in s.
#
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
#
# A substring is a contiguous sequence of characters in a string.

from collections import defaultdict

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = 3
        if len(s) < n:
            return 0

        left = 0
        our_dict = defaultdict(int)
        result = 0
        for right in range(len(s)):
            our_dict[s[right]] += 1

            if (right - left + 1) < n:
                continue

            while (right - left + 1) != n and left <= right:
                if s[left] in our_dict:
                    our_dict[s[left]] -= 1
                    if our_dict[s[left]] == 0: our_dict.pop(s[left])
                left += 1

            if len(our_dict) == 3:
                result += 1
        return result

s = "xyzzaz"
x = Solution()
print(x.countGoodSubstrings(s))