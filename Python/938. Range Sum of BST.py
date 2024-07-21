# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].
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
    def rangeSumBST1(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        OurSum = 0
        OurStack = deque()
        tempNode = root
        while tempNode or OurStack:
            while tempNode:
                OurStack.append(tempNode)
                if tempNode.val < low: break
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            OurSum += tempNode.val if low <= tempNode.val <= high else 0
            tempNode = tempNode.right
        return OurSum

root = [10,5,15,3,7,"null",18]; low = 7; high = 15
OurRoot = built_simply_binary_tree(root)
X = Solution()
print(X.rangeSumBST1(OurRoot, low, high))











