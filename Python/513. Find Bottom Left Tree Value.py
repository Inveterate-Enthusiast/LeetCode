# Given the root of a binary tree, return the leftmost value in the last row of the tree.

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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        _queue = deque()
        _queue.append(root)
        ansVal = None
        while _queue:
            curLen = len(_queue)
            for i in range(curLen):
                tempNode = _queue.popleft()
                if i == 0:
                    ansVal = tempNode.val
                if tempNode.left: _queue.append(tempNode.left)
                if tempNode.right: _queue.append(tempNode.right)
        return ansVal

    def findBottomLeftValue1(self, root: Optional[TreeNode]) -> int:
        self._tuple = (0, root.val) # level and value

        def bfs(node: Optional[TreeNode], level: Optional[int]) -> Optional[Tuple[int, int]]:
            if not node:
                return (0, 0)

            self._tuple = self._tuple if self._tuple[0] >= level else (level, node.val)
            left = bfs(node.left, level + 1)
            right = bfs(node.right, level + 1)

        bfs(root, 1)

        return self._tuple[1]

null = "null"
root = [1,2,3,4,null,5,6,null,null,7]
OurRoot = build(root)
X = Solution()
print(X.findBottomLeftValue1(OurRoot))
