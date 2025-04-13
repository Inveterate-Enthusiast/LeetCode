# You are given a string s consisting of lowercase English letters.
# Your task is to find the maximum difference between the frequency of two characters in the string such that:
#
# One of the characters has an even frequency in the string.
# The other character has an odd frequency in the string.
# Return the maximum difference, calculated as the frequency of the character with an odd frequency
# minus the frequency of the character with an even frequency.

from collections import defaultdict

class Solution:
    def maxDifference(self, s: str) -> int:
        our_dict = defaultdict(int)
        for i in s:
            our_dict[i] += 1

        max_odd = max([v for k, v in our_dict.items() if (v % 2) != 0])
        min_even = min([v for k, v in our_dict.items() if (v % 2) == 0])
        return max_odd - min_even

    def maxDifference1(self, s: str) -> int:
        our_dict = defaultdict(int)
        for i in s:
            our_dict[i] += 1

        max_odd, min_even = float("-inf"), float("inf")
        for key, value in our_dict.items():
            if (value % 2) == 0:
                min_even = min(min_even, value)
            else:
                max_odd = max(max_odd, value)

        return max_odd - min_even

s = "aaaaabbc"
x = Solution()
print(x.maxDifference(s))