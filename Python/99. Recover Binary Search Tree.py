# You are given the root of a binary search tree (BST),
# where the values of exactly two nodes of the tree were swapped by mistake.
# Recover the tree without changing its structure.
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
    def recoverTree1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        OurStack = deque()
        tempNode = root
        ReplaceList = deque()
        prevNode = None
        while tempNode or OurStack:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left

            tempNode = OurStack.pop()
            if prevNode:
                if prevNode.val >= tempNode.val:
                    ReplaceList.append((prevNode, tempNode))
            prevNode = tempNode
            tempNode = tempNode.right

        ReplaceList[0][0].val, ReplaceList[-1][1].val = ReplaceList[-1][1].val, ReplaceList[0][0].val

    def recoverTree2(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        OurStack = deque()
        tempNode = root
        OurList = []
        while tempNode or OurStack:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            OurList.append((tempNode, tempNode.val))
            tempNode = tempNode.right

        OurNewList = sorted(OurList, key = lambda x: x[1])

        for i in range(len(OurList)):
            if OurList[i][1] != OurNewList[i][1]:
                OurList[i][0].val, OurNewList[i][0].val = OurNewList[i][0].val, OurList[i][0].val
                break

    def recoverTree3(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            pass

        OurStack = deque()
        tempNode = root
        OurList = []
        while tempNode or OurStack:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            OurList.append((tempNode, tempNode.val))
            tempNode = tempNode.right

        newSortedList = sorted(OurList, key=lambda x: x[1])

        for i in range(len(OurList)):
            if OurList[i][1] != newSortedList[i][1]:
                OurList[i][0].val, newSortedList[i][0].val = newSortedList[i][0].val, OurList[i][0].val
                break

    def recoverTree4(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            pass

        OurStack = deque()
        tempNode = root
        OurList = deque()

        while OurStack or tempNode:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            OurList.append(tempNode)
            tempNode = tempNode.right

        newList = sorted(OurList, key=lambda x: x.val)

        for i in range(len(OurList)):
            if OurList[i].val != newList[i].val:
                OurList[i].val, newList[i].val = newList[i].val, OurList[i].val
                break

    def recoverTree5(self, root: Optional[TreeNode]) -> None:
        OurStack = deque()
        tempNode = root
        curList = []
        while tempNode or OurStack:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            curList.append(tempNode)
            tempNode = tempNode.right

        newList = sorted(curList, key=lambda x: x.val)

        for index in range(len(curList)):
            if curList[index].val != newList[index].val:
                curList[index].val, newList[index].val = newList[index].val, curList[index].val
                break





root = [1,3,"null","null",2]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.recoverTree4(OurRoot))








