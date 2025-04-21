# You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.
#
# The permutation difference between s and t is defined as the sum of the absolute difference between the index
# of the occurrence of each character in s and the index of the occurrence of the same character in t.
#
# Return the permutation difference between s and t.

from collections import defaultdict

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_dict, t_dict = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            s_dict[s[i]] = i
            t_dict[t[i]] = i

        result = 0
        for char, index in s_dict.items():
            result += (abs(index - t_dict[char]))

        return result

    def findPermutationDifference1(self, s: str, t: str) -> int:
        s_dict = defaultdict(int)
        for index, i in enumerate(s):
            s_dict[i] = index

        result = 0
        for index, i in enumerate(t):
            result += (abs(index - s_dict[i]))

        return result

s = "abc"
t = "bac"
x = Solution()
print(x.findPermutationDifference1(s, t))