# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        our_set = {chr(i) for i in range(97, 122+1)}
        return our_set == set(sentence)

    def checkIfPangram1(self, sentence: str) -> bool:
        return len(set(sentence)) >= 26

sentence = "thequickbrownfoxjumpsoverthelazydog"
x = Solution()
print(x.checkIfPangram1(sentence))