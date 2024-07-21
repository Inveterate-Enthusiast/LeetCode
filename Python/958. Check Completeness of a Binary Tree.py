# Given the root of a binary tree, determine if it is a complete binary tree.
#
# In a complete binary tree, every level, except possibly the last, is completely filled,
# and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built(lst:Optional[list]) -> Optional[TreeNode]:
    if not lst:
        return TreeNode

    _queue = deque()
    _root = TreeNode(val=lst[0])
    _queue.append(_root)
    i = 1
    while i < len(lst):
        curNode = _queue.popleft()
        if i < len(lst) and lst[i] != "null":
            curNode.left = TreeNode(val=lst[i])
            _queue.append(curNode.left)
        i += 1

        if i < len(lst) and lst[i] != "null":
            curNode.right = TreeNode(val=lst[i])
            _queue.append(curNode.right)
        i += 1
    return _root

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        _queue = deque()
        _queue.append(root)
        findEnd = False
        while _queue:
            curNode = _queue.popleft()
            if not curNode:
                findEnd = True
            else:
                if findEnd: return False
                _queue.append(curNode.left)
                _queue.append(curNode.right)
        return True

root = [1,2,3,4,"null",5]
OurRoot = built(root)
X = Solution()
print(X.isCompleteTree(OurRoot))



