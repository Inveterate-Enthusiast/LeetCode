# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
#
# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
#
# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
from typing import List

class Solution:
    def canVisitAllRooms1(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True

        OurDict = dict()
        newKeys, usedKeys = set(), set()
        for index, room in enumerate(rooms):
            OurDict[index] = room

        newKeys = newKeys.union(set(OurDict.pop(0)))
        while newKeys:
            curKey = newKeys.pop()
            if curKey not in usedKeys:
                if curKey in OurDict:
                    newKeys = newKeys.union(OurDict.pop(curKey))
                    usedKeys.add(curKey)

        return not bool(OurDict)




rooms = [[1,3],[3,0,1],[2],[0]]
X = Solution()
print(X.canVisitAllRooms1(rooms))



