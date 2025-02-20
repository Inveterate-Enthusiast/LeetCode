# Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies
# of each letter from 'a' to 'z' between word1 and word2 is at most 3.
#
# Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.
#
# The frequency of a letter x is the number of times it occurs in the string.

from collections import defaultdict

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for i in word1:
            dict1[i] += 1

        for i in word2:
            dict2[i] += 1

        for k, v in dict1.items():
            if abs(v - dict2.get(k, 0)) > 3:
                return False

        for k, v in dict2.items():
            if abs(v - dict1.get(k, 0)) > 3:
                return False

        return True

word1 = "abcdeef"
word2 = "abaaacc"
x = Solution()
print(x.checkAlmostEquivalent(word1, word2))