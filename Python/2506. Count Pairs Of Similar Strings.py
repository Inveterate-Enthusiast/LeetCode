# You are given a 0-indexed string array words.
#
# Two strings are similar if they consist of the same characters.
#
# For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
# However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
# Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.

from typing import List
from collections import defaultdict

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        our_dict = defaultdict(int)
        result = 0
        for i in words:
            j = frozenset(i)
            result += our_dict[j]
            our_dict[j] += 1

        return result

words = ["aba","aabb","abcd","bac","aabc"]
x = Solution()
print(x.similarPairs(words))