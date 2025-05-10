# You are given an array of equal-length strings words. Assume that the length of each string is n.
#
# Each string words[i] can be converted into a difference integer array difference[i] of length n - 1
# where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference
# between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.
#
# For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
# All the strings in words have the same difference integer array, except one. You should find that string.
#
# Return the string in words that has different difference integer array.

from typing import List
from collections import defaultdict

class Solution:
    def oddString(self, words: List[str]) -> str:
        our_dict = dict()
        char = "a"
        char_num = ord(char)
        char_num_temp = char_num
        while char != "z":
            char = chr(char_num_temp)
            our_dict[char] = (char_num_temp - char_num)
            char_num_temp += 1

        dict_char, dict_freq = defaultdict(set), defaultdict(int)
        n = len(words[0])
        result = set()

        for word in words:
            dif = tuple((our_dict[word[i]] - our_dict[word[(i - 1)]]) for i in range(1, n))
            dict_freq[dif] += 1
            dict_char[dif].add(word)
            if dict_freq[dif] > 1:
                result = result.difference((dict_char[dif]))
            else:
                result.add(word)

        return result.pop() if result else str()


words = ["adc","wzy","abc"]
x = Solution()
print(x.oddString(words))