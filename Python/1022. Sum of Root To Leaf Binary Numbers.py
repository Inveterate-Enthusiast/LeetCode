# You are given the root of a binary tree where each node has a value 0 or 1.
# Each root-to-leaf path represents a binary number starting with the most significant bit.
#
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
# Return the sum of these numbers.
#
# The test cases are generated so that the answer fits in a 32-bits integer.
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
    def sumRootToLeaf1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        OurQueue = deque()
        OurQueue.append((root, str(root.val)))
        OurGeneralQueue = deque()
        while OurQueue:
            tempNode, OurStr = OurQueue.popleft()
            if not tempNode.left and not tempNode.right:
                OurGeneralQueue.append(OurStr)
                continue
            if tempNode.left: OurQueue.append((tempNode.left, OurStr + str(tempNode.left.val)))
            if tempNode.right: OurQueue.append((tempNode.right, OurStr + str(tempNode.right.val)))

        OurSum = 0
        while OurGeneralQueue:
            OurSum += int(OurGeneralQueue.popleft(), 2)

        return OurSum


root = [0]
OurRoot = built_simply_binary_tree(root)
X = Solution()
print(X.sumRootToLeaf1(OurRoot))





