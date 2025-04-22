# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
#
# Return the number of special letters in word.

from collections import  defaultdict

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        our_dict = defaultdict(int)
        result = set()
        for i in word:
            if our_dict[i.swapcase()] > 0:
                result.add(i.lower())
            our_dict[i] += 1

        return len(result)

word = "aaAbcBC"
x = Solution()
print(x.numberOfSpecialChars(word))