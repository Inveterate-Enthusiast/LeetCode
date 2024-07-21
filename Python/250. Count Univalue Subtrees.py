# Given the root of a binary tree, return the number of uni-value subtrees.
#
# A uni-value subtree means all nodes of the subtree have the same value.
from typing import List, Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build(lst:List) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()

    _queue = deque()
    root = TreeNode(val=lst[0])
    _queue.append(root)
    i = 1
    while i < len(lst):
        tempNode = _queue.popleft()
        if i < len(lst) and lst[i] != "null":
            tempNode.left = TreeNode(val=lst[i])
            _queue.append(tempNode.left)
        i += 1
        if i < len(lst) and lst[i] != "null":
            tempNode.right = TreeNode(val=lst[i])
            _queue.append(tempNode.right)
        i += 1
    return root

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        _stack1 = deque(); _stack2 = deque()
        OurCount = 0; _stack1.append(root)
        _dict = defaultdict(set)
        while _stack1:
            tempNode = _stack1.pop()
            _dict[tempNode].add(tempNode.val)
            _stack2.append(tempNode)

            if tempNode.left: _stack1.append(tempNode.left)
            if tempNode.right: _stack1.append(tempNode.right)

        while _stack2:
            tempNode = _stack2.pop()
            if tempNode.left: _dict[tempNode] = _dict[tempNode].union(_dict[tempNode.left])
            if tempNode.right: _dict[tempNode] = _dict[tempNode].union(_dict[tempNode.right])
            OurCount += (len(_dict[tempNode]) == 1)

        return OurCount

    def countUnivalSubtrees1(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def preorder(node:Optional[TreeNode], _set:Optional[set]) -> Optional[set]:
            if not node:
                return _set
            left = preorder(node.left, _set)
            right = preorder(node.right, _set)
            _set = left.union(right)
            _set.add(node.val)
            self.count += (len(_set) == 1)
            return _set

        preorder(root, set())
        return self.count

root = [5,1,5,5,5,"null",5]
OurRoot = build(root)
X = Solution()
print(X.countUnivalSubtrees1(OurRoot))