# You are given a string s consisting of lowercase English letters ('a' to 'z').
#
# Your task is to:
#
# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.
#
# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
#
# The frequency of a letter x is the number of times it occurs in the string.

from collections import defaultdict

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        dict_vowels, dict_consonants = defaultdict(int), defaultdict(int)
        max_vowels, max_consonants = 0, 0
        for i in s:
            if i in vowels:
                dict_vowels[i] += 1
                max_vowels = max(max_vowels, dict_vowels[i])
            else:
                dict_consonants[i] += 1
                max_consonants = max(max_consonants, dict_consonants[i])

        return max_vowels + max_consonants

s = "successes"
x = Solution()
print(x.maxFreqSum(s))