# Given the root of a binary tree,
# return the bottom-up level order traversal of its nodes' values.
# (i.e., from left to right, level by level from leaf to root).
from typing import Optional, List
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
    def levelOrderBottom1(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        OurQueue = deque()
        OurQueue.append((root, 1))
        OurList = []
        while OurQueue:
            tempNode, level = OurQueue.popleft()
            if level > len(OurList):
                OurList.append([tempNode.val])
            else:
                OurList[level-1].append(tempNode.val)

            if tempNode.left: OurQueue.append((tempNode.left, level+1))
            if tempNode.right: OurQueue.append((tempNode.right, level+1))

        for i in range(len(OurList)//2):
            OurList[i], OurList[-i-1] = OurList[-i-1], OurList[i]

        return OurList

    def levelOrderBottom2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        OurQueue = deque()
        OurQueue.append(root)
        OurList = []
        while OurQueue:
            curLen = len(OurQueue)
            level_nodes = []
            for _ in range(curLen):
                tempNode = OurQueue.popleft()
                level_nodes.append(tempNode.val)
                if tempNode.left: OurQueue.append(tempNode.left)
                if tempNode.right: OurQueue.append(tempNode.right)
            OurList.append(level_nodes)

        for i in range(len(OurList)//2):
            OurList[i], OurList[-i-1] = OurList[-i-1], OurList[i]

        return OurList

root = [3,9,20,"null","null",15,7]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.levelOrderBottom2(OurRoot))













