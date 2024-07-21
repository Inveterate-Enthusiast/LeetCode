# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built_simple_binary_tree(lst:list) -> Optional[TreeNode]:
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
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        OurStack = deque()
        tempNode = root
        prevNode = None
        while OurStack or tempNode:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            if prevNode:
                if prevNode.val >= tempNode.val: return False
            prevNode = tempNode
            tempNode = tempNode.right
        return True

root = [2,1,3]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.isValidBST1(OurRoot))









