# Given the root of a binary tree and an integer targetSum,
# return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
# Each path should be returned as a list of the node values, not node references.
#
# A root-to-leaf path is a path starting from the root and ending at any leaf node.
# A leaf is a node with no children.
from typing import List, Optional
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
    rootNode = TreeNode(val=lst[0])
    OurQueue.append(rootNode)
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

    return rootNode

class Solution:
    def pathSum1(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        OurQueue = deque()
        OurQueue.append((root, targetSum, []))
        OurList = []
        while OurQueue:
            tempNode, curSum, curList = OurQueue.popleft()

            if not tempNode.left and not tempNode.right:
                if (curSum - tempNode.val) == 0: OurList.append(curList+[tempNode.val])
                continue


            if tempNode.left: OurQueue.append((tempNode.left, curSum - tempNode.val, curList + [tempNode.val]))
            if tempNode.right: OurQueue.append((tempNode.right, curSum - tempNode.val, curList + [tempNode.val]))

        return OurList

    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        OurList = []
        def helpDef(root: Optional[TreeNode], targetSum: int, curList: Optional[List[int]] = []):
            if not root:
                return
            elif not root.left and not root.right:
                if (targetSum) == 0: OurList.append(curList)

            if root.left: helpDef(root.left, targetSum - root.left.val, curList + [root.left.val])
            if root.right: helpDef(root.right, targetSum - root.right.val, curList + [root.right.val])

        helpDef(root, targetSum - root.val, [root.val])
        return OurList

    def pathSum3(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        OurList = []

        def helpDef(node: Optional[TreeNode], curSum: int, curList: List[int]):
            if not node:
                return
            elif not node.left and not node.right:
                if (curSum - node.val) == 0: OurList.append(curList+[node.val])
                return

            helpDef(node = node.left, curSum = (curSum - node.val), curList = (curList + [node.val]))
            helpDef(node=node.right, curSum=(curSum - node.val), curList=(curList + [node.val]))

        helpDef(root, targetSum, [])
        return OurList

    def pathSum4(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        OurList = []
        OurQueue = deque()
        OurQueue.append((root, targetSum, []))
        while OurQueue:
            tempNode, curSum, curList = OurQueue.popleft()

            if not tempNode.left and not tempNode.right:
                if (curSum - tempNode.val) == 0: OurList.append(curList + [tempNode.val])
                continue

            if tempNode.left: OurQueue.append((tempNode.left, (curSum - tempNode.val), (curList + [tempNode.val])))
            if tempNode.right: OurQueue.append((tempNode.right, (curSum - tempNode.val), (curList + [tempNode.val])))
        return OurList

root = [7,0,"null",-1,-6,"null",1,"null","null",-7]; targetSum = 0
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.pathSum4(OurRoot, targetSum))









