# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

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

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return list()
        OurQueue = deque()
        OurQueue.append(root)
        ansList = list()
        while OurQueue:
            curLen = len(OurQueue)
            for _ in range(curLen):
                tempNode = OurQueue.popleft()
                if tempNode.left: OurQueue.append(tempNode.left)
                if tempNode.right: OurQueue.append(tempNode.right)
            else:
                ansList.append(tempNode.val)
        return ansList


