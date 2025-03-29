# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.

from typing import List
from collections import defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        our_dict = defaultdict(int)
        for i in chars:
            our_dict[i] += 1

        result = 0
        for word in words:
            temp_dict = our_dict.copy()
            for i in word:
                if temp_dict[i] == 0:
                    temp_dict = our_dict
                    break
                temp_dict[i] -= 1
            if temp_dict != our_dict:
                result += len(word)

        return result

words = ["cat","bt","hat","tree"]
chars = "atach"
x = Solution()
print(x.countCharacters(words, chars))