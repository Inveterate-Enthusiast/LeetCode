# In a binary tree, a lonely node is a node that is the only child of its parent node.
# The root of the tree is not lonely because it does not have a parent node.
#
# Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree.
# Return the list in any order.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built_simply_binary_tree(lst:list) -> Optional[TreeNode]:
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
    def getLonelyNodes1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        OurQueue = deque()
        OurQueue.append((root, False))
        OurList = []
        while OurQueue:
            tempNode, curFlag = OurQueue.popleft()

            if curFlag:
                OurList.append(tempNode.val)

            if tempNode.left and tempNode.right:
                tempFlag = False
            else:
                tempFlag = True

            if tempNode.left: OurQueue.append((tempNode.left, tempFlag))
            if tempNode.right: OurQueue.append((tempNode.right, tempFlag))


        return OurList

root = [11,99,88,77,"null","null",66,55,"null","null",44,33,"null","null",22]
OurRoot = built_simply_binary_tree(root)
X = Solution()
print(X.getLonelyNodes1(OurRoot))








