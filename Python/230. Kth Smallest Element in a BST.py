# Given the root of a binary search tree, and an integer k,
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built(lst: list) -> Optional[TreeNode]:
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
    def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        tempNode = root
        OurStack = deque()
        while OurStack or tempNode:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            k -= 1
            if not k: return tempNode.val
            tempNode = tempNode.right
        return tempNode

root = [3,1,4,"null",2]; k = 1
OurRoot = built(root)
X = Solution()
print(X.kthSmallest1(OurRoot, k))







