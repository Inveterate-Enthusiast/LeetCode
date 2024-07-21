# Given the root of a binary tree, flatten the tree into a "linked list":
#
# The "linked list" should use the same TreeNode class
# where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
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
    def flatten1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        OurQueue = deque()
        OurStack = deque()
        OurStack.append(root)
        while OurStack:
            tempNode = OurStack.pop()
            OurQueue.append(tempNode)
            if tempNode.right: OurStack.append(tempNode.right)
            if tempNode.left: OurStack.append(tempNode.left)

        while OurQueue:
            tempNode = OurQueue.popleft()
            tempNode.left = None
            tempNode.right = OurQueue[0] if OurQueue else None

    def flatten2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        tempNode = root
        while tempNode:
            if tempNode.left:
                rightMost = tempNode.left
                while rightMost.right:
                    rightMost = rightMost.right
                rightMost.right = tempNode.right
                tempNode.right = tempNode.left
                tempNode.left = None
            tempNode = tempNode.right

    def flatten3(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        if not root.left and not root.right:
            return root

        OurQueue = deque(); OurStack = deque()
        OurStack.append(root)
        while OurStack:
            tempNode = OurStack.pop()
            OurQueue.append(tempNode)
            if tempNode.right: OurStack.append(tempNode.right)
            if tempNode.left: OurStack.append(tempNode.left)

        while OurQueue:
            tempNode = OurQueue.popleft()
            if OurQueue: tempNode.right = OurQueue[0]
            tempNode.left = None

    def flatten4(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        if not root.left and not root.right:
            return root

        tempNode = root
        while tempNode:
            if tempNode.left:
                curRoot = tempNode.left
                while curRoot.right:
                    curRoot = curRoot.right
                curRoot.right = tempNode.right
                tempNode.right = tempNode.left
                tempNode.left = None
            tempNode = tempNode.right




root = [1,2,5,3,4,"null",6]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.flatten3(OurRoot))







