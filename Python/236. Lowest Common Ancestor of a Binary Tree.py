# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
# (where we allow a node to be a descendant of itself).”
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
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not p or not q:
            return None
        if not root:
            return None

        root.level = 1
        OurQueue = deque()
        OurQueue.append((root, set([root]))) # node and its parents
        find_p = find_q = False
        while OurQueue and (not find_p or not find_q):
            tempNode, curSet = OurQueue.popleft()

            if tempNode is p: find_p = True; p_set = curSet
            if tempNode is q: find_q = True; q_set = curSet

            if tempNode.left:
                tempNode.left.level = tempNode.level + 1
                OurQueue.append((tempNode.left, curSet.union(set([tempNode.left]))))

            if tempNode.right:
                tempNode.right.level = tempNode.level + 1
                OurQueue.append((tempNode.right, curSet.union(set([tempNode.right]))))

        parents = p_set.intersection(q_set)
        LCA, i = None, float("-inf")
        for parent in parents:
            if parent.level > i:
                LCA, i = parent, parent.level

        return LCA

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root is p or root is q:
            return root

        leftNode = self.lowestCommonAncestor2(root.left, p, q)
        rightNode = self.lowestCommonAncestor2(root.right, p, q)

        if not leftNode:
            return rightNode
        elif not rightNode:
            return leftNode
        else:
            return root



root = [37,-34,-48,"null",-100,-101,48,"null","null","null","null",-54,"null",-71,-22,"null","null","null",8]; p = -71; q = 8
OurRoot = build(root)
OurP, OurQ = identify(OurRoot, p, q)
X = Solution()
print(X.lowestCommonAncestor2(OurRoot, OurP, OurQ))
