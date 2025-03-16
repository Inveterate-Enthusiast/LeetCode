# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.

from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        our_dict = defaultdict(int)

        n = len(s)
        left, result = 0, 0
        for right in range(n):
            our_dict[s[right]] += 1
            while left < right and our_dict[s[right]] > 2:
                our_dict[s[left]] -= 1
                left += 1
            result = max(result, (right - left + 1))

        return result

s = "bcbbbcba"
x = Solution()
print(x.maximumLengthSubstring(s))