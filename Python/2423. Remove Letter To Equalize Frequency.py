# You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.
#
# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.
#
# Note:
#
# The frequency of a letter x is the number of times it occurs in the string.
# You must remove exactly one letter and cannot choose to do nothing.

from collections import defaultdict

class Solution:
    def equalFrequency(self, word: str) -> bool:
        dict_char = defaultdict(int)
        for i in word:
            dict_char[i] += 1

        dict_freq = defaultdict(int)
        for char, freq in dict_char.items():
            dict_freq[freq] += 1

        list_freq = list(dict_freq.keys())
        if (len(list_freq) == 1) and ((list_freq[0] == 1) or dict_freq[list_freq[0]] == 1):
            return True
        elif not len(list_freq) == 2:
            return False

        freq1, freq2 = list_freq[0], list_freq[1]
        if (dict_freq[freq1] == 1) or (dict_freq[freq2] == 1):
            if ((freq1 == 1) and (dict_freq[freq1] == 1)) or ((freq2 == 1) and (dict_freq[freq2] == 1)):
                return True
            x = freq1 if dict_freq[freq1] == 1 else freq2
            y = freq1 if x == freq2 else freq2
            if (y == (x - 1)):
                return True

        return False




word = "aaaabbbbccc"
x = Solution()
print(x.equalFrequency(word))