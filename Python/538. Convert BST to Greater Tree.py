# Given the root of a Binary Search Tree (BST),
# convert it to a Greater Tree such that every key of the original BST is changed to the original
# key plus the sum of all keys greater than the original key in BST.
#
# As a reminder, a binary search tree is a tree that satisfies these constraints:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
from typing import List, Optional, Tuple
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build(lst:list) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()
    OurQueue = deque()
    root = TreeNode(val=lst[0])
    OurQueue.append(root)
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
    return root

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.tempSum = 0
        def dfs(node: Optional[TreeNode]) -> Optional[int]:
            if not node:
                return 0
            dfs(node.right)
            node.val += self.tempSum
            self.tempSum = node.val
            dfs(node.left)
            return self.tempSum

        dfs(root)

        return root

    def convertBST1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.tempSum = 0

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node:
                dfs(node.right)
                node.val += self.tempSum
                self.tempSum = node.val
                dfs(node.left)
            return node

        return dfs(root)

null = "null"
root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
OurRoot = build(root)
X = Solution()
print(X.convertBST(OurRoot))