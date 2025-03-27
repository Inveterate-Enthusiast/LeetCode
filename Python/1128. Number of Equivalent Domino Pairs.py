# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only
# if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
#
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

from typing import List
from collections import defaultdict
from math import comb

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        our_dict = defaultdict(int)
        for i in dominoes:
            our_dict[frozenset(i)] += 1

        result = 0
        for key, value in our_dict.items():
            if value > 1:
                result += comb(value, 2)

        return result

dominoes = [[1,2],[2,1],[3,4],[5,6]]
x = Solution()
print(x.numEquivDominoPairs(dominoes))