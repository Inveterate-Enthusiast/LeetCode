# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

from typing import List
from collections import defaultdict

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for i in words1:
            dict1[i] += 1

        for i in words2:
            dict2[i] += 1

        result = 0
        for k, v in dict1.items():
            if (v == 1) and (dict2.get(k, 0) == 1):
                result += 1

        return result

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
x = Solution()
print(x.countWords(words1, words2))