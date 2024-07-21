# A binary tree is uni-valued if every node in the tree has the same value.
#
# Given the root of a binary tree,
# return true if the given tree is uni-valued, or false otherwise.
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
    def isUnivalTree1(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        OurStack = deque()
        OurStack.append(root)
        OurSet = set()
        while OurStack:
            tempNode = OurStack.pop()
            OurSet.add(tempNode.val)
            if len(OurSet) > 1:
                return False
            if tempNode.left: OurStack.append(tempNode.left)
            if tempNode.right: OurStack.append(tempNode.right)
        return True

root = [1,1,1,1,1,"null",1]
OurRoot = built_simply_binary_tree(root)
X = Solution()
print(X.isUnivalTree1(OurRoot))



