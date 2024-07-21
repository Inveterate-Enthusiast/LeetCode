# In the world of Dota2, there are two parties: the Radiant and the Dire.
#
# The Dota2 senate consists of senators coming from two parties.
# Now the Senate wants to decide on a change in the Dota2 game.
# The voting for this change is a round-based procedure.
# In each round, each senator can exercise one of the two rights:
#
# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party,
# he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging.
# The character 'R' and 'D' represent the Radiant party and the Dire party.
# Then if there are n senators, the size of the given string will be n.
#
# The round-based procedure starts from the first senator to the last senator in the given order.
# This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.
#
# Suppose every senator is smart enough and will play the best strategy for his own party.
# Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        OurDict = {
            "R": [deque(), "Radiant"],
            "D": [deque(), "Dire"]
        }
        for index, senator in enumerate(senate):
            OurDict[senator][0].append(index)

        while OurDict["R"][0] and OurDict["D"][0]:
            for i in range(max(rLen := len(OurDict["R"][0]), dLen := len(OurDict["D"][0]))):
                if OurDict["R"][0] and OurDict["D"][0]:
                    rIndex = OurDict["R"][0].popleft(); rLen -= 1
                    dIndex = OurDict["D"][0].popleft(); dLen -= 1

                    if rLen >= 0 and dLen >= 0:
                        if rIndex < dIndex: OurDict["R"][0].append(rIndex)
                        if dIndex < rIndex: OurDict["D"][0].append(dIndex)
                    else:
                        if rLen >= 0: OurDict["R"][0].append(rIndex)
                        if dLen >= 0: OurDict["D"][0].append(dIndex)

        return OurDict["R"][1] if OurDict["R"][0] else OurDict["D"][1]


senate = "DDRRR"
X = Solution()
print(X.predictPartyVictory(senate))






