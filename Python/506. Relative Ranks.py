# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition.
# All the scores are guaranteed to be unique.
#
# The athletes are placed based on their scores, where the 1st place athlete has the highest score,
# the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
#
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        our_dict = dict()
        result = list()
        gold, silver, bronze = "Gold Medal", "Silver Medal", "Bronze Medal"
        score_sorted = sorted(score, reverse=True)

        for i in range(len(score_sorted)):
            if i > 2:
                our_dict[score_sorted[i]] = i+1
            elif i == 0:
                our_dict[score_sorted[i]] = gold
            elif i == 1:
                our_dict[score_sorted[i]] = silver
            elif i == 2:
                our_dict[score_sorted[i]] = bronze

        for s in score:
            result.append(str(our_dict[s]))

        return result

    def findRelativeRanks1(self, score: List[int]) -> List[str]:
        our_dict = dict()
        result = list()
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        score_sorted = sorted(score, reverse=True)

        for i in range(len(score_sorted)):
            if i > 2: our_dict[score_sorted[i]] = i+1
            else: our_dict[score_sorted[i]] = ranks[i]

        for s in score:
            result.append(str(our_dict[s]))

        return result

score = [5,4,3,2,1]
x = Solution()
print(x.findRelativeRanks1(score))