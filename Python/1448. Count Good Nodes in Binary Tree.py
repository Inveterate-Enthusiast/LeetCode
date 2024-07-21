# Given a binary tree root, a node X in the tree is named good
# if in the path from root to X there are no nodes with a value greater than X.
#
# Return the number of good nodes in the binary tree.

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built_simple_binary_tree(lst:list) -> Optional[TreeNode]:
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
    def goodNodes1(self, root: TreeNode) -> int:
        if not root:
            return 0

        OurSet = set()
        OurGoodCounter = 0
        OurMaxValue = root.val
        OurStack = deque()
        tempNode = root
        while tempNode or OurStack:
            while tempNode:
                if tempNode not in OurSet:
                    if tempNode.val >= OurMaxValue:
                        OurGoodCounter += 1
                        OurMaxValue = tempNode.val
                    else:
                        tempNode.val = OurMaxValue
                    OurSet.add(tempNode)
                OurStack.append(tempNode)
                tempNode = tempNode.left

            tempNode = OurStack.pop()
            OurMaxValue = tempNode.val
            tempNode = tempNode.right
        return OurGoodCounter

root = [-103,1,"null",3,"null",1,5]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.goodNodes1(OurRoot))










