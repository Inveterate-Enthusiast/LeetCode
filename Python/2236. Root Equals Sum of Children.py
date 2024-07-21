# You are given the root of a binary tree that consists of exactly 3 nodes:
# the root, its left child, and its right child.
#
# Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.
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
    def checkTree1(self, root: Optional[TreeNode]) -> bool:
        return root.val == (root.left.val + root.right.val)

root = [10,4,6]
OurRoot = built_simply_binary_tree(root)
X = Solution()
print(X.checkTree1(OurRoot))












