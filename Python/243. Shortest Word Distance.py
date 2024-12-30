# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2,
# return the shortest distance between these two words in the list.
from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        left_index, left_word = float("-inf"), word1
        our_set = {word1, word2}
        result = float("inf")
        for index, word in enumerate(wordsDict):
            if word == left_word:
                left_index = index
            elif word in our_set:
                result = min(result, (index - left_index))
                left_index = index
                left_word = word
        return result

    def shortestDistance1(self, wordsDict: List[str], word1: str, word2: str) -> int:
        result = len(wordsDict)
        pos1, pos2 = -1, -1
        for index, word in enumerate(wordsDict):
            if word == word1: pos1 = index
            if word == word2: pos2 = index

            if pos1 != (-1) and pos2 != (-1):
                result = min(result, abs(pos1 - pos2))
        return result

wordsDict = ["this","is","a","long","sentence","is","fun","day","today","sunny","weather","is","a","day","tuesday","this","sentence","run","running","rainy"]
word1 = "weather"
word2 = "long"

X = Solution()
print(X.shortestDistance1(wordsDict, word1, word2))