# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none)
# deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
from typing import List, Optional
from collections import deque, defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        _dict = defaultdict(bool)
        ans_number = 0

        def is_sub(sub_str) -> bool:
            index = -1
            for char in sub_str:
                index = s.find(char, index+1)
                if index == (-1): return False
            return True

        for word in words:
            if word in _dict:
                ans_number += _dict[word]
            else:
                ans = is_sub(word)
                _dict[word] = ans
                ans_number += ans

        return ans_number

    def numMatchingSubseq1(self, s: str, words: List[str]) -> int:
        _dict = defaultdict(bool)
        ans_number = 0
        len_s = len(s)

        def is_sub(sub_str) -> bool:
            len_sub = len(sub_str)
            i = j = 0
            while i < len_s and j < len_sub:
                if s[i] == sub_str[j]:
                    j += 1
                i += 1
            return j == len_sub

        for word in words:
            if word in _dict:
                ans_number += _dict[word]
            else:
                ans = is_sub(word)
                _dict[word] = ans
                ans_number += ans
        return ans_number

s = "dsahjpjauf"; words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
X = Solution()
print(X.numMatchingSubseq(s, words))