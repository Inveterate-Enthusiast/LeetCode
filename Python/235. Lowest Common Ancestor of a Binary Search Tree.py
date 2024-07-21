# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
from typing import List, Optional, Tuple
from collections import deque

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

def identify(root, p, q) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
    OurQueue = deque()
    OurQueue.append(root)
    OurP = OurQ = None
    while OurQueue and (not OurQ or not OurP):
        tempNode = OurQueue.popleft()
        if tempNode.val == p: OurP = tempNode
        if tempNode.val == q: OurQ = tempNode

        if tempNode.left: OurQueue.append(tempNode.left)
        if tempNode.right: OurQueue.append(tempNode.right)

    return OurP, OurQ

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root is p or root is q:
            return root

        leftNode = self.lowestCommonAncestor(root.left, p, q)
        rightNode = self.lowestCommonAncestor(root.right, p, q)

        if not leftNode:
            return rightNode
        elif not rightNode:
            return leftNode
        else:
            return root

root = [6,2,8,0,4,7,9,"null","null",3,5]; p = 2; q = 8
OurRoot = build(root)
OurP, OurQ = identify(OurRoot, p, q)
X = Solution()
print(X.lowestCommonAncestor(OurRoot, OurP, OurQ).val)