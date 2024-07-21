# Given a root node reference of a BST and a key,
# delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
from typing import Optional, List
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
    def deleteNode1(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        pass



root = [5,3,6,2,4,"null",7]; key = 3
OurRoot = built(root)
X = Solution()
print(X.deleteNode1(OurRoot, key))

