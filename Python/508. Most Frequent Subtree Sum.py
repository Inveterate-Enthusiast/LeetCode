# Given the root of a binary tree, return the most frequent subtree sum.
# If there is a tie, return all the values with the highest frequency in any order.
#
# The subtree sum of a node is defined as the sum of all the node
# values formed by the subtree rooted at that node (including the node itself).
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
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self._dict = defaultdict(int)
        self._max = 0
        self._list = list()

        def dfs(node: Optional[TreeNode]) -> Optional[int]:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self._dict[curSum := (node.val + left + right)] += 1
            self._max = max(self._max, self._dict[curSum])
            return curSum

        dfs(root)

        for key, value in self._dict.items():
            if value == self._max:
                self._list.append(key)
        return self._list

    def findFrequentTreeSum1(self, root: Optional[TreeNode]) -> List[int]:
        self._dict = defaultdict(int)
        self._max = 0

        def dfs(node:Optional[TreeNode]) -> Optional[int]:
            if not node:
                return 0
            leftSum, rightSum = dfs(node.left), dfs(node.right)
            self._dict[curSum := (node.val + leftSum + rightSum)] += 1
            self._max = max(self._max, self._dict[curSum])
            return curSum

        dfs(root)

        return [key for key, val in self._dict.items() if val == self._max]

root = [5,2,-3]
OurRoot = build(root)
X = Solution()
print(X.findFrequentTreeSum1(OurRoot))