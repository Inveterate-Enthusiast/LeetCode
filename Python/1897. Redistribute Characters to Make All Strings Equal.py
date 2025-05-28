# You are given an array of strings words (0-indexed).
#
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string,
# and move any character from words[i] to any position in words[j].
#
# Return true if you can make every string in words equal using any number of operations, and false otherwise.

from typing import List
from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        our_dict = defaultdict(int)
        for word in words:
            for char in word:
                our_dict[char] += 1

        n = len(words)
        for char, freq in our_dict.items():
            if (freq % n) != 0:
                return False

        return True

words = ["abc","aabc","bc"]
x = Solution()
print(x.makeEqual(words))