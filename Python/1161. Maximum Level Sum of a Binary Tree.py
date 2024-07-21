# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
#
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.


from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built(lst:list) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()

    OurQueue = deque()
    OurRoot = TreeNode(val=lst[0])
    OurQueue.append(OurRoot)
    i = 1
    while i < len(lst):
        tempNode = OurQueue.popleft()
        if i < len(lst) and lst[i] != "null":
            tempNode.left = TreeNode(val=lst[i])
            OurQueue.append(tempNode.left)
        i += 1
        if i < len(lst) and lst[i] != "null":
            tempNode.right = TreeNode(val=lst[i])
            OurQueue.append(tempNode.right)
        i += 1
    return OurRoot

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        if not root.left and not root.right:
            return 1

        OurQueue = deque()
        ans_list = [None, float("-inf")]
        OurQueue.append((root, 1)) #node and its level
        while OurQueue:
            curLen = len(OurQueue)
            curSum = 0
            for _ in range(curLen):
                tempNode, tempLevel = OurQueue.popleft()
                curSum += tempNode.val
                if tempNode.left: OurQueue.append((tempNode.left, tempLevel + 1))
                if tempNode.right: OurQueue.append((tempNode.right, tempLevel + 1))
            else:
                ans_list = ans_list if ans_list[1] >= curSum else [tempLevel, curSum]

        return ans_list[0]

root = [1,7,0,7,-8,"null","null"]
OurRoot = built(root)
X = Solution()
print(X.maxLevelSum(OurRoot))


