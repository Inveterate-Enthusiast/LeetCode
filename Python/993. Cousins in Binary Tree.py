# Given the root of a binary tree with unique values
# and the values of two different nodes of the tree x and y,
# return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
#
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
#
# Note that in a binary tree, the root node is at the depth 0,
# and children of each depth k node are at the depth k + 1.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built_simply_binary_tree(lst:list) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()

    OurQueue = deque()
    OurRoot = TreeNode(val=lst[0])
    OurQueue.append(OurRoot)
    i = 1
    while i < len(lst):
        tempNode = OurQueue.popleft()
        if i < len(lst) and lst[i] != "null":
            tempNode.left = TreeNode(val=lst[i])
            OurQueue.append(tempNode.left)
        i += 1

        if i < len(lst) and lst[i] != "null":
            tempNode.right = TreeNode(val=lst[i])
            OurQueue.append(tempNode.right)
        i += 1

    return OurRoot

class Solution:
    def isCousins1(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        OurQueue = deque()
        OurQueue.append((root, 1))
        OurX = None; OurY = None
        while OurQueue:
            tempNode, level = OurQueue.popleft()

            if OurX and OurY:
                return (OurX[0] is not OurY[0]) and (OurX[1] == OurY[1])

            if tempNode.left:
                OurQueue.append((tempNode.left, level+1))
                if tempNode.left.val == x: OurX = (tempNode, level+1)
                if tempNode.left.val == y: OurY = (tempNode, level+1)

            if tempNode.right:
                OurQueue.append((tempNode.right, level+1))
                if tempNode.right.val == x: OurX = (tempNode, level+1)
                if tempNode.right.val == y: OurY = (tempNode, level+1)

        return False

root = [1,2,3,"null",4]; x=2; y=3
OurRoot = built_simply_binary_tree(root)
X = Solution()
print(X.isCousins1(OurRoot, x, y))










