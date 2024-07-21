# You are given the root of a full binary tree with the following properties:
#
# Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
# Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
# The evaluation of a node is as follows:
#
# If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
# Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
# Return the boolean result of evaluating the root node.
#
# A full binary tree is a binary tree where each node has either 0 or 2 children.
#
# A leaf node is a node that has zero children.

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
    def transformAns(self, one, two, operator):
        assert operator == 2 or operator == 3, "Operator error"
        if operator == 2:
            return one or two
        elif operator == 3:
            return one and two


    def evaluateTree1(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        OurStack = deque()
        OurDict = dict()
        OurStack.append((root, False))
        while OurStack:
            tempNode, OurFlag = OurStack.pop()
            if not OurFlag:
                OurStack.append((tempNode, True))
                if tempNode.right: OurStack.append((tempNode.right, False))
                if tempNode.left: OurStack.append((tempNode.left, False))
            else:
                if tempNode.val < 2:
                    OurDict[tempNode] = True if tempNode.val else False
                else:
                    leftAns = OurDict.get(tempNode.left, False)
                    rightAns = OurDict.get(tempNode.right, False)
                    OurDict[tempNode] = self.transformAns(leftAns, rightAns, tempNode.val)
        return OurDict[root]

root = [0]
OurRoot = built_simply_binary_tree(root)
X = Solution()
print(X.evaluateTree1(OurRoot))








