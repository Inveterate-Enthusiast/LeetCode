# Given a string paragraph and a string array of the banned words banned,
# return the most frequent word that is not banned. It is guaranteed there is at least one
# word that is not banned, and that the answer is unique.
#
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

from typing import List
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        freq_dict = defaultdict(int)
        word = str()
        for _, letter in enumerate(paragraph.lower()):
            if letter.isalpha():
                word += letter
            else:
                if word: freq_dict[word] += 1
                word = str()
        else:
            if word: freq_dict[word] += 1

        ban_set = set(banned)
        result = [None, 0]
        for word, freq in freq_dict.items():
            if not word in ban_set:
                result = result if result[1] > freq else [word, freq]
        return result[0]

paragraph = "Bob"
banned = ["hit"]
x = Solution()
print(x.mostCommonWord(paragraph, banned))