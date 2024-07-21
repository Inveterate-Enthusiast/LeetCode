# Given the root of a binary search tree and a node p in it,
# return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree,
# return null.
#
# The successor of a node p is the node with the smallest key greater than p.val.
from typing import List, Optional, Tuple
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build(lst:list) -> Optional[TreeNode]:
    if not lst:
        return TreeNode(val=None)
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

def identify(root:TreeNode, p:Optional[int]) -> Optional[TreeNode]:
    OurQueue = deque()
    OurQueue.append(root)
    OurP = None
    while OurQueue and not OurP:
        tempNode = OurQueue.popleft()
        if tempNode.val == p: OurP = tempNode

        if tempNode.left: OurQueue.append(tempNode.left)
        if tempNode.right: OurQueue.append(tempNode.right)

    return OurP

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        _stack = deque(); _queue = deque()
        tempNode = root; flag = False
        while _stack or tempNode:
            while tempNode:
                _stack.append(tempNode)
                tempNode = tempNode.left
            tempNode = _stack.pop()
            if flag: _queue.append(tempNode)
            if tempNode is p: flag = True
            tempNode = tempNode.right

        Successor = None
        for tempNode in _queue:
            if tempNode.val > p.val:
                if not Successor:
                    Successor = tempNode
                else:
                    Successor = Successor if Successor.val < tempNode.val else tempNode

        return Successor


root = [2,1,3]; p = 1
OurRoot = build(root)
OurP = identify(OurRoot, p)
X = Solution()
print(X.inorderSuccessor(OurRoot, OurP))