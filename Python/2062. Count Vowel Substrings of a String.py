# A substring is a contiguous (non-empty) sequence of characters within a string.
#
# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
#
# Given a string word, return the number of vowel substrings in word.

from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        our_set = {"a", "e", "i", "o", "u"}
        our_dict = defaultdict(int)
        our_start = None
        result = 0
        for index, char in enumerate(word):
            if char in our_set:
                if our_start is None:
                    our_start = index
                our_dict[char] = index
                if len(our_dict) == len(our_set):
                    result += min(our_dict.values()) - our_start + 1
            else:
                our_dict = defaultdict(int)
                our_start = None

        return result

word = "aaeiiouu"
x = Solution()
print(x.countVowelSubstrings(word))