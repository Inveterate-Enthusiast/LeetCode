# Given the root of a complete binary tree, return the number of the nodes in the tree.
#
# According to Wikipedia, every level, except possibly the last,
# is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible.
# It can have between 1 and 2h nodes inclusive at the last level h.
#
# Design an algorithm that runs in less than O(n) time complexity.

from collections import deque
from typing import Optional

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
        curNode = OurQueue.popleft()
        if i < len(lst) and lst[i] != "null":
            curNode.left = TreeNode(val=lst[i])
            OurQueue.append(curNode.left)
        i += 1

        if i < len(lst) and lst[i] != "null":
            curNode.right = TreeNode(val=lst[i])
            OurQueue.append(curNode.right)
        i += 1
    return rootNode

class Solution:
    def countNodes1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        tempNode = root
        OurLevel = 0
        while tempNode:
            OurLevel += 1
            tempNode = tempNode.left

        tempNode = root
        OurCheck = 0
        while tempNode:
            OurCheck += 1
            tempNode = tempNode.right

        if OurLevel == OurCheck:
            OurResult = 2**(OurLevel)-1
        else:
            OurResult = 1 + self.countNodes1(root.left) + self.countNodes1(root.right)
        return OurResult

    def countNodes2(self, root: Optional[TreeNode]) -> int: #inorder traversale
        OurStack = deque()
        tempNode = root
        OurCount = 0
        while OurStack or tempNode:
            while tempNode:
                OurCount += 1
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            tempNode = tempNode.right
        return OurCount




root = [1,2,3,4]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.countNodes2(OurRoot))






