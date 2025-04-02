# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
#
# Return the number of consistent strings in the array words.

from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        our_set = set([i for i in allowed])
        result = 0
        for word in words:
            flag = True
            for i in word:
                if not i in our_set:
                    flag = False
                    break

            if flag: result += 1

        return result

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
x = Solution()
print(x.countConsistentStrings(allowed, words))