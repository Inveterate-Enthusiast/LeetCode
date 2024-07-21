# Given two integer arrays preorder and inorder where preorder is the preorder traversal
# of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootNode = TreeNode(val=preorder[0])
        index = inorder.index(preorder[0])
        rootNode.left = self.buildTree1(preorder[1:index + 1], inorder[:index])
        rootNode.right = self.buildTree1(preorder[index + 1:], inorder[index + 1:])
        return rootNode

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootNode = None
        OurStack = deque()
        OurDict = {x : i for i, x in enumerate(inorder)}

        for x in preorder:
            if not rootNode:
                rootNode = tempNode = TreeNode(val=x)
            elif OurDict[x] < OurDict[tempNode.val]:
                OurStack.append(tempNode)
                tempNode.left = tempNode = TreeNode(val=x)
            else:
                while OurStack and OurDict[OurStack[-1].val] < OurDict[x]:
                    tempNode = OurStack.pop()
                tempNode.right = tempNode = TreeNode(val=x)

        return rootNode

    def buildTree3(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        curRoot = TreeNode(val=preorder[0])
        index = inorder.index(curRoot.val)
        curRoot.left = self.buildTree3(preorder[1:index + 1], inorder[:index])
        curRoot.right = self.buildTree3(preorder[index + 1:], inorder[index + 1:])
        return curRoot

    def buildTree4(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootNode = None
        OurStack = deque()
        OurDict = {x : i for i, x in enumerate(inorder)}

        for x in preorder:
            if not rootNode:
                rootNode = tempNode = TreeNode(val=x)
            elif OurDict[x] < OurDict[tempNode.val]:
                OurStack.append(tempNode)
                tempNode.left = tempNode = TreeNode(val=x)
            else:
                while OurStack and OurDict[OurStack[-1].val] < OurDict[x]:
                    tempNode = OurStack.pop()
                tempNode.right = tempNode = TreeNode(val=x)
        return rootNode

    def buildTree5(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootNode = TreeNode(val=preorder[0])
        index = inorder.index(rootNode.val)
        rootNode.left = self.buildTree5(preorder[1:index+1], inorder[:index])
        rootNode.right = self.buildTree5(preorder[index+1:], inorder[index+1:])
        return rootNode

    def buildTree6(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        OurStack = deque()
        rootNode = None
        OurDict = {x : i for i, x in enumerate(inorder)}

        for x in preorder:
            if not rootNode:
                rootNode = tempNode = TreeNode(val=x)
            elif OurDict[x] < OurDict[tempNode.val]:
                OurStack.append(tempNode)
                tempNode.left = tempNode = TreeNode(val=x)
            else:
                while OurStack and OurDict[OurStack[-1].val] < OurDict[x]:
                    tempNode = OurStack.pop()
                tempNode.right = tempNode = TreeNode(val=x)

        return rootNode

    def buildTree7(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootNode = TreeNode(val=preorder[0])
        index = inorder.index(rootNode.val)
        rootNode.left = self.buildTree7(preorder[1:index+1], inorder[:index])
        rootNode.right = self.buildTree7(preorder[index+1:], inorder[index+1:])
        return rootNode

    def buildTree8(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        OurStack = deque()
        rootNode = None
        OurDict = {x : i for i, x in enumerate(inorder)}

        for value in preorder:
            if not rootNode:
                rootNode = tempNode = TreeNode(val=value)
            elif OurDict[value] < OurDict[tempNode.val]:
                OurStack.append(tempNode)
                tempNode.left = tempNode = TreeNode(val=value)
            else:
                while OurStack and OurDict[OurStack[-1].val] < OurDict[value]:
                    tempNode = OurStack.pop()
                tempNode.right = tempNode = TreeNode(val=value)
        return rootNode




preorder = [3,9,10,20,15,11,7]; inorder = [10,9,3,11,15,20,7]
X = Solution()
print(X.buildTree8(preorder, inorder))














