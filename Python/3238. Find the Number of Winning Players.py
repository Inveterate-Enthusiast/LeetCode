# You are given an integer n representing the number of players in a game and a 2D array pick where pick[i] = [xi, yi]
# represents that the player xi picked a ball of color yi.
#
# Player i wins the game if they pick strictly more than i balls of the same color. In other words,
#
# Player 0 wins if they pick any ball.
# Player 1 wins if they pick at least two balls of the same color.
# ...
# Player i wins if they pick at leasti + 1 balls of the same color.
# Return the number of players who win the game.
#
# Note that multiple players can win the game.

from typing import List
from collections import defaultdict

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        our_dict = defaultdict(lambda: defaultdict(int))
        for player, ball in pick:
            our_dict[player][ball] += 1

        result = 0
        for player, balls in our_dict.items():
            for color, value in balls.items():
                if player < value:
                    result += 1
                    break

        return result

n = 4
pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
x = Solution()
print(x.winningPlayerCount(n, pick))