# You are given an integer array ranks and a character array suits. You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].
#
# The following are the types of poker hands you can make from best to worst:
#
# "Flush": Five cards of the same suit.
# "Three of a Kind": Three cards of the same rank.
# "Pair": Two cards of the same rank.
# "High Card": Any single card.
# Return a string representing the best type of poker hand you can make with the given cards.
#
# Note that the return values are case-sensitive.

from typing import List
from collections import defaultdict

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        suits_dict = defaultdict(int)
        ranks_dict = defaultdict(int)
        for i in suits:
            suits_dict[i] += 1
            if suits_dict[i] == 5:
                return "Flush"

        cur_max = 0
        for i in ranks:
            ranks_dict[i] += 1
            cur_max = max(cur_max, ranks_dict[i])

        if cur_max >= 3:
            return "Three of a Kind"
        elif cur_max == 2:
            return "Pair"

        return "High Card"

    def bestHand1(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        our_dict = defaultdict(int)
        cur_max = 0
        for i in ranks:
            our_dict[i] += 1
            cur_max = max(cur_max, our_dict[i])

        if cur_max >= 3:
            return "Three of a Kind"
        elif cur_max == 2:
            return "Pair"

        return "High Card"

ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]
x = Solution()
print(x.bestHand(ranks, suits))