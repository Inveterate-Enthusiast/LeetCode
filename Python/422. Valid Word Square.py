# Given an array of strings words, return true if it forms a valid word square.
#
# A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).
from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        max_len = len(words)
        for word in words:
            max_len = max(max_len, len(word))

        our_len = len(words)

        for i in range(max_len):
            for j in range(i+1, max_len):
                if i >= our_len and j >= our_len:
                    continue
                elif i >= our_len or j >= our_len:
                    return False
                elif j >= len(words[i]) and i >= len(words[j]):
                    continue
                elif j >= len(words[i]) or i >= len(words[j]):
                    return False
                elif words[i][j] != words[j][i]:
                    return False
        return True
        


words = ["abcd","bnrt","crm","dt"]
x = Solution()
print(x.validWordSquare(words))