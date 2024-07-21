# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers.
# Test cases are generated so that the answer will fit in a 32-bit integer.
#
# A leaf node is a node with no children.
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
    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        OurList = list()
        OurQueue = deque()
        OurQueue.append((root, str(root.val)))
        while OurQueue:
            tempNode, tempNumber = OurQueue.popleft()

            if not tempNode.left and not tempNode.right:
                OurList.append(int(tempNumber))

            if tempNode.left: OurQueue.append((tempNode.left, tempNumber + str(tempNode.left.val)))
            if tempNode.right: OurQueue.append((tempNode.right, tempNumber + str(tempNode.right.val)))

        return sum(OurList)

    def sumNumbers2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        OurSum = 0
        OurQueue = deque()
        OurQueue.append((root, str(root.val)))
        while OurQueue:
            tempNode, tempSum = OurQueue.popleft()

            if not tempNode.left and not tempNode.right:
                OurSum += int(tempSum)

            if tempNode.left: OurQueue.append((tempNode.left, tempSum + str(tempNode.left.val)))
            if tempNode.right: OurQueue.append((tempNode.right, tempSum + str(tempNode.right.val)))
        return OurSum


root = [1,2,3]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.sumNumbers2(OurRoot))




