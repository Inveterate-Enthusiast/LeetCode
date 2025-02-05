# There is a special keyboard with all keys in a single row.
#
# Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25). Initially,
# your finger is at index 0. To type a character, you have to move your finger to the index of the desired character.
# The time taken to move your finger from index i to index j is |i - j|.
#
# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

from collections import defaultdict

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        our_dict = defaultdict(int)
        for index, key in enumerate(keyboard):
            our_dict[key] = index

        if len(word) == 1:
            return our_dict[word[0]]

        prev_idx = 0
        result = 0
        for i, key in enumerate(word):
            result += (abs(prev_idx - (prev_idx := our_dict[key])))

        return result

keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "cba"
x = Solution()
print(x.calculateTime(keyboard, word))