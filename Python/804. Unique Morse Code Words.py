# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
#
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
#
# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...".
# We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha_dict = dict()
        for index, num in enumerate(range(97, 122+1)):
            alpha_dict[chr(num)] = morse[index]

        result_set = set()
        for word in words:
            word_tmp = str()
            for a in word:
                word_tmp = word_tmp + alpha_dict[a]
            result_set.add(word_tmp)
        return len(result_set)

words = ["gin","zen","gig","msg"]
x = Solution()
print(x.uniqueMorseRepresentations(words))