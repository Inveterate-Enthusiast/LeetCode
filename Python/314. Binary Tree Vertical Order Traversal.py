# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
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
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return list()

        _queue = deque()
        _dict = defaultdict(list)
        _queue.append((root, 1))
        _min = 1; ansList = list()
        while _queue:
            curLen = len(_queue)
            for _ in range(curLen):
                tempNode, tempVert = _queue.popleft()
                _dict[tempVert].append(tempNode.val)
                _min = min(_min, tempVert)

                if tempNode.left: _queue.append((tempNode.left, tempVert - 1))
                if tempNode.right: _queue.append((tempNode.right, tempVert + 1))

        while _min in _dict:
            ansList.append(_dict[_min])
            _min += 1

        return ansList


root = [3,9,20,"null","null",15,7]
OurRoot = build(root)
X = Solution()
print(X.verticalOrder(OurRoot))