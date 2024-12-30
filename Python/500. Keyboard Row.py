# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row
# of American keyboard like the image below.
#
# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.
#
# In the American keyboard:
#
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set_first = set("qwertyuiop")
        set_second = set("asdfghjkl")
        set_third = set("zxcvbnm")
        result = list()
        for word in words:
            a = b = c = True
            for letter in word:
                if a:
                    a = letter.lower() in set_first
                if b:
                    b = letter.lower() in set_second
                if c:
                    c = letter.lower() in set_third
            if max(a, b, c): result.append(word)
        return result
    def findWords1(self, words: List[str]) -> List[str]:
        set_first = set("qwertyuiop")
        set_second = set("asdfghjkl")
        set_third = set("zxcvbnm")
        result = list()
        for word in words:
            x = set(word.lower())
            if x <= set_first or x <= set_second or x <= set_third:
                result.append(word)
        return result

words = ["Alaska", "Hello","Dad","Peace"]
x = Solution()
print(x.findWords1(words))