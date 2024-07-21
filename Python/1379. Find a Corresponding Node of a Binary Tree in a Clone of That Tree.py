# Given two binary trees original and cloned and given a reference to a node target in the original tree.
#
# The cloned tree is a copy of the original tree.
#
# Return a reference to the same node in the cloned tree.
#
# Note that you are not allowed to change any of the two trees
# or the target node and the answer must be a reference to a node in the cloned tree.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def built_simply_binary_tree(lst:list) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()

    OurQueue = deque()
    OurRoot = TreeNode(x=lst[0])
    OurQueue.append(OurRoot)
    i = 1
    while i < len(lst):
        tempNode = OurQueue.popleft()
        if i < len(lst) and lst[i] != "null":
            tempNode.left = TreeNode(x=lst[i])
            OurQueue.append(tempNode.left)
        i += 1

        if i < len(lst) and lst[i] != "null":
            tempNode.right = TreeNode(x=lst[i])
            OurQueue.append(tempNode.right)
        i += 1

    return OurRoot

def find_reference_target_node(root: Optional[TreeNode], targetValue) -> Optional[TreeNode]:
    if not root:
        return None
    OurQueue = deque()
    OurQueue.append(root)
    while OurQueue:
        tempNode = OurQueue.popleft()
        if tempNode.val == targetValue:
            return tempNode
        if tempNode.left: OurQueue.append(tempNode.left)
        if tempNode.right: OurQueue.append(tempNode.right)
    return None

class Solution:
    def getTargetCopy1(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or not target:
            return None

        OurQueue1 = deque(); OurQueue2 = deque()
        OurQueue1.append(original); OurQueue2.append(cloned)
        while OurQueue1 and OurQueue2:
            tempNode1 = OurQueue1.popleft()
            tempNode2 = OurQueue2.popleft()

            if tempNode1 is target:
                return tempNode2

            if tempNode1.left: OurQueue1.append(tempNode1.left)
            if tempNode2.left: OurQueue2.append(tempNode2.left)
            if tempNode1.right: OurQueue1.append(tempNode1.right)
            if tempNode2.right: OurQueue2.append(tempNode2.right)
        return None

tree = [7,4,3,"null","null",6,19]; target = 3
OurTree = built_simply_binary_tree(tree)
OurTarget = find_reference_target_node(OurTree, target)
X = Solution()
print(X.getTargetCopy1(OurTree, OurTree, OurTarget))













