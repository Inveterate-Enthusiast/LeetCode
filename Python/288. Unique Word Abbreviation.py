# The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last letter,
# and its last letter. If a word has only two characters, then it is an abbreviation of itself.
#
# For example:
#
# dog --> d1g because there is one letter between the first letter 'd' and the last letter 'g'.
# internationalization --> i18n because there are 18 letters between the first letter 'i' and the last letter 'n'.
# it --> it because any word with only two characters is an abbreviation of itself.
# Implement the ValidWordAbbr class:
#
# ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary of words.
# boolean isUnique(string word) Returns true if either of the following conditions are met (otherwise returns false):
# There is no word in dictionary whose abbreviation is equal to word's abbreviation.
# For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same.
from typing import List, Optional

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self._dict = dict()
        self._abbr = dict()
        for word in dictionary:
            if word not in self._dict:
                cur_abbr = self.__get_abbr(word)
                self._dict[word] = cur_abbr
                self._abbr[cur_abbr] = self._abbr.get(cur_abbr, 0) + 1

    def isUnique(self, word: str) -> bool:
        cur_abbr = self.__get_abbr(word)
        if word in self._dict and self._abbr[cur_abbr] == 1: return True
        return not(cur_abbr in self._abbr)

    def __get_abbr(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + str(len(word)-2) + word[-1]



X = ValidWordAbbr(["a","a"])
print(X.isUnique("a"))