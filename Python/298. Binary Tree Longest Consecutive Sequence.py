# Given the root of a binary tree, return the length of the longest consecutive sequence path.
#
# A consecutive sequence path is a path where the values increase by one along the path.
#
# Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.
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
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        _queue = deque()
        _queue.append((root, 1))
        maxLen = float("-inf")
        while _queue:
            tempNode, curLen = _queue.popleft()
            maxLen = max(maxLen, curLen)
            if tempNode.left: _queue.append((tempNode.left, ((curLen+1) if tempNode.left.val == (tempNode.val + 1) else 1)))
            if tempNode.right: _queue.append((tempNode.right, ((curLen + 1) if tempNode.right.val == (tempNode.val + 1) else 1)))
        return maxLen


root = [1,"null",3,2,4,"null","null","null",5]
OurRoot = build(root)
X = Solution()
print(X.longestConsecutive(OurRoot))