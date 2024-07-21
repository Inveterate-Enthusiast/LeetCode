# Given the root of a binary tree, invert the tree, and return its root.

from typing import Optional
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
    rootNode = TreeNode(val=lst[0])
    OurQueue.append(rootNode)
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

    return rootNode

class Solution:
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        OurStack = deque()
        OurStack.append(root)
        while OurStack:
            tempNode = OurStack.pop()
            leftNode = tempNode.left
            tempNode.left = tempNode.right
            tempNode.right = leftNode
            if tempNode.left: OurStack.append(tempNode.left)
            if tempNode.right: OurStack.append(tempNode.right)
        return root

    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # через рекурсию
        if root is None:
            return None
        root.left, root.right = self.invertTree2(root.right), self.invertTree2(root.left)
        return root

root = [4,2,7,1,3,6,9]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.invertTree2(OurRoot))