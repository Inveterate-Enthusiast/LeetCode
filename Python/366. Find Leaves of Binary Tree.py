# Given the root of a binary tree, collect a tree's nodes as if you were doing this:
#
# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.
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
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self._list = deque()
        self._dict = defaultdict(list)

        def bfs(node: Optional[TreeNode]) -> Optional[int]:
            if not node:
                return (-1)
            leftLevel = bfs(node.left)
            rightLevel = bfs(node.right)
            self._dict[curLevel:=(max(leftLevel, rightLevel)+1)].append(node.val)
            return curLevel

        bfs(root)
        i = 0
        while i in self._dict:
            self._list.append(self._dict[i])
            i += 1

        return self._list

    def findLeaves1(self, root: Optional[TreeNode]) -> List[List[int]]:
        self._list = deque()

        def bfs(node: Optional[TreeNode]) -> Optional[int]:
            if not node:
                return (-1)
            left = bfs(node.left)
            right = bfs(node.right)
            curLevel = max(left, right) + 1
            if curLevel >= len(self._list):
                self._list.append(list())
            self._list[curLevel].append(node.val)
            return curLevel

        bfs(root)
        return self._list


root = [1,2,3,4,5]
OurRoot = build(root)
X = Solution()
print(X.findLeaves1(OurRoot))