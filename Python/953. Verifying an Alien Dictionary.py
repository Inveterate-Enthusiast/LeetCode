# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true
# if and only if the given words are sorted lexicographically in this alien language.

from typing import List
from collections import defaultdict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True

        our_dict = defaultdict(int)
        for index, letter in enumerate(order):
            our_dict[letter] = index

        for i in range(1, len(words)):
            j = 0
            while j < len(words[i]) and j < len(words[i-1]):
                if our_dict[words[i][j]] > our_dict[words[i-1][j]]:
                    break
                elif our_dict[words[i][j]] < our_dict[words[i-1][j]]:
                    return False
                j += 1
            else:
                if not (len(words[i]) == len(words[i-1])) and j >= len(words[i]): return False
        return True

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
x = Solution()
print(x.isAlienSorted(words, order))