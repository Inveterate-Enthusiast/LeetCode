# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
#
# Besides the root, each house has one and only one parent house. After a tour,
# the smart thief realized that all houses in this place form a binary tree.
# It will automatically contact the police if two directly-linked houses were broken into on the same night.
#
# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
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
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> Optional[Tuple[int, int]]:
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            return (node.val + left[1] + right[1], (max(left[0], left[1]) + max(right[0], right[1])))

        return max(dfs(root))



root = [3,2,3,"null",3,"null",1]
OurRoot = build(root)
X = Solution()
print(X.rob(OurRoot))