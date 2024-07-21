# Given two integer arrays inorder and postorder
# where inorder is the inorder traversal of a binary tree
# and postorder is the postorder traversal of the same tree, construct and return the binary tree.

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        rootNode = None
        OurStack = deque()
        OurDict = {x : i for i, x in enumerate(inorder)}

        for x in reversed(postorder):
            if not rootNode:
                rootNode = tempNode = TreeNode(val=x)
            elif OurDict[x] > OurDict[tempNode.val]:
                OurStack.append(tempNode)
                tempNode.right = tempNode = TreeNode(val=x)
            else:
                while OurStack and OurDict[OurStack[-1].val] > OurDict[x]:
                    tempNode = OurStack.pop()
                tempNode.left = tempNode = TreeNode(val=x)

        return rootNode

    def buildTree2(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        rootNode = TreeNode(val=postorder[-1])
        index = inorder.index(rootNode.val)
        rootNode.left = self.buildTree2(inorder[:index], postorder[:index])
        rootNode.right = self.buildTree2(inorder[index+1:], postorder[index:-1])
        return rootNode

    def buildTree3(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        rootNode = TreeNode(val=postorder[-1])
        index = inorder.index(rootNode.val)
        rootNode.left = self.buildTree3(inorder[:index], postorder[:index])
        rootNode.right = self.buildTree3(inorder[index+1:], postorder[index:-1])
        return rootNode

    def buildTree4(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        OurStack = deque()
        rootNode = None
        OurDict = {x : i for i, x in enumerate(inorder)}

        for x in postorder[::-1]:
            if not rootNode:
                rootNode = tempNode = TreeNode(val=x)
            elif OurDict[x] > OurDict[tempNode.val]:
                OurStack.append(tempNode)
                tempNode.right = tempNode = TreeNode(val=x)
            else:
                while OurStack and OurDict[OurStack[-1].val] > OurDict[x]:
                    tempNode = OurStack.pop()
                tempNode.left = tempNode = TreeNode(val=x)

        return rootNode

    def buildTree5(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        rootNode = TreeNode(val=postorder[-1])
        index = inorder.index(rootNode.val)
        rootNode.left = self.buildTree5(inorder[:index], postorder[:index])
        rootNode.right = self.buildTree5(inorder[index+1:], postorder[index:-1])
        return rootNode

    def buildTree6(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        OurStack = deque()
        rootNode = None
        OurDict = {x : i for i, x in enumerate(inorder)}

        for value in postorder[::-1]:
            if not rootNode:
                rootNode = tempNode = TreeNode(val = value)
            elif OurDict[value] > OurDict[tempNode.val]:
                OurStack.append(tempNode)
                tempNode.right = tempNode = TreeNode(val = value)
            else:
                while OurStack and OurDict[OurStack[-1].val] > OurDict[value]:
                    tempNode = OurStack.pop()
                tempNode.left = tempNode = TreeNode(val = value)
        return rootNode



inorder = [9,3,15,20,7]; postorder = [9,15,7,20,3]
X = Solution()
print(X.buildTree5(inorder, postorder))










