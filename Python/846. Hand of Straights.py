# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize,
# and consists of groupSize consecutive cards.
#
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
# return true if she can rearrange the cards, or false otherwise.


from typing import List, Optional
from collections import deque, defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        handLen = len(hand)
        if not hand or (handLen % groupSize):
            return False

        _dict = {i: hand.count(i) for i in set(hand)}
        curSize = groupSize; curElement = None
        while _dict:
            if not curSize:
                curSize = groupSize
                curElement = None

            if curElement is None:
                curElement = min(_dict)
                if _dict[curElement] == 1:
                    del _dict[curElement]
                else:
                    _dict[curElement] -= 1
                curSize -= 1
            else:
                if curElement+1 not in _dict:
                    return False
                curElement += 1
                if _dict[curElement] == 1:
                    del _dict[curElement]
                else:
                    _dict[curElement] -= 1
                curSize -= 1

        return True

    def isNStraightHand1(self, hand: List[int], groupSize: int) -> bool:
        handLen = len(hand)
        if not hand or (handLen % groupSize):
            return False

        newHand = deque(sorted(hand))
        _dict = defaultdict(deque)
        while newHand:
            if (curElement := newHand.popleft()) not in _dict:
                curLen = 1
            else:
                curLen = _dict[curElement].popleft() + 1
                if not _dict[curElement]: _dict.pop(curElement)

            if curLen != groupSize:
                _dict[curElement + 1].append(curLen)


        return not bool(_dict)


hand = [1,2,3]; groupSize = 1
X = Solution()
print(X.isNStraightHand1(hand, groupSize))
