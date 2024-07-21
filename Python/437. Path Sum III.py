# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build(lst:list) ->Optional[TreeNode]:
    if not lst:
        return TreeNode()
    OurQueue = deque()
    root = TreeNode(val=lst[0])
    OurQueue.append(root)
    i = 1
    while i < len(lst):
        curNode = OurQueue.popleft()
        if i < len(lst) and lst[i] != "null":
            curNode.left = TreeNode(val=lst[i])
            OurQueue.append(curNode.left)
        i += 1

        if i < len(lst) and lst[i] != "null":
            curNode.right = TreeNode(val=lst[i])
            OurQueue.append(curNode.right)
        i += 1
    return root


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return int(root.val==targetSum)
        OurQueue = deque()
        OurQueue.append((root, [targetSum]))
        ansCount = 0
        while OurQueue:
            curNode, curList = OurQueue.popleft()
            for i in range(len(curList)):
                curList[i] -= curNode.val
                if curList[i] == 0: ansCount += 1

            curList.append(targetSum)

            if curNode.left: OurQueue.append((curNode.left, curList.copy()))
            if curNode.right: OurQueue.append((curNode.right, curList.copy()))

        return ansCount

root = [10,5,-3,3,2,"null",11,3,-2,"null",1]; targetSum = 8
OurRoot = build(root)
X = Solution()
print(X.pathSum(OurRoot, targetSum))



