# You are given the root of a binary tree.
#
# A ZigZag path for a binary tree is defined as follow:
#
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
#
# Return the longest ZigZag path contained in that tree.
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        OurQueue = deque()
        OurQueue.append((root, 0, 0))
        maxPath = 0
        while OurQueue:
            curNode, leftPath, rightPath = OurQueue.popleft()
            maxPath = max(maxPath, leftPath, rightPath)
            if curNode.left: OurQueue.append((curNode.left, rightPath + 1, 0))
            if curNode.right: OurQueue.append((curNode.right, 0, leftPath + 1))

        return maxPath



root = [1,1,1,"null",1,"null","null",1,1,"null",1]
OurRoot = build(root)
X = Solution()
print(X.longestZigZag(OurRoot))




