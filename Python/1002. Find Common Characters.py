# Given a string array words, return an array
# of all characters that show up in all strings within the words (including duplicates).
# You may return the answer in any order.

from typing import List, Optional, Dict
import string

class Solution:
    def intersection_dict(self, dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
        if not dict1 or not dict2:
            return None

        ansDict = dict()

        for key, value in dict1.items():
            if key in dict2:
                ansDict[key] = min(dict1[key], dict2[key])

        return ansDict

    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return list()
        _dict = {i: words[0].count(i) for i in set(words[0])}

        for i in range(1, len(words)):
            curDict = {m: words[i].count(m) for m in set(words[i])}
            _dict = self.intersection_dict(_dict, curDict)
            if not _dict:
                return list()

        return [k for k, v in _dict.items() for _ in range(v)]



words = ["bella", "label", "roller"]
X = Solution()
print(X.commonChars(words))