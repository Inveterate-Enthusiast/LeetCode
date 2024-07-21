# Design a data structure that will be initialized with a string array,
# and then it should answer queries of the shortest distance between two different strings from the array.
#
# Implement the WordDistance class:
#
# WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
# int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
from typing import Optional, List

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.__word_dict = dict()
        for index, word in enumerate(wordsDict):
            if word not in self.__word_dict:
                self.__word_dict[word] = [index]
            else:
                self.__word_dict[word].append(index)



    def shortest(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        array1 = self.__word_dict[word1]
        array2 = self.__word_dict[word2]
        point1 = point2 = 0
        minDiff = float('inf')

        while point1 < len(array1) and point2 < len(array2):
            curDiff = abs(array1[point1] - array2[point2])
            minDiff = min(minDiff, curDiff)

            if array1[point1] < array2[point2]:
                point1 += 1
            else:
                point2 += 1

        return minDiff



X = WordDistance(["practice","makes","perfect","coding","makes"])
print(X.shortest(word1="makes", word2="practice"))
print(X.shortest(word1="makes", word2="coding"))




