# You are given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
#
# Return the shuffled string.

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        result = [str()] * n

        for i in range(n):
            result[indices[i]] = s[i]

        return "".join(result)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
x = Solution()
print(x.restoreString(s, indices))