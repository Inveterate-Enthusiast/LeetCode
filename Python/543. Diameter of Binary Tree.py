# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DoubleLL:
    head = None

    class Node:
        def __init__(self, element=None, next=None, prev=None):
            self.element = element
            self.next = next
            self.prev = prev

    def append(self, element):
        if not self.head:
            self.head = self.Node(element=element)
        elif not self.head.next:
            self.head.next = self.head.prev = self.Node(element=element, next=self.head, prev=self.head)
        else:
            self.head.prev.next = self.Node(element=element, next=self.head, prev=self.head.prev)
            self.head.prev = self.head.prev.next

    def pop(self):
        if not self.head:
            return None
        elif not self.head.next:
            Node = self.head
            self.head = self.head.next
        else:
            Node = self.head.prev
            if not self.head.prev.prev is self.head:
                self.head.prev = self.head.prev.prev
                self.head.prev.next = self.head
            else:
                self.head.next = self.head.prev = None
        return Node.element

    def popleft(self):
        if not self.head:
            return None
        Node = self.head
        if not self.head.next:
            self.head = self.head.next
        elif self.head.prev.prev is self.head:
            self.head = self.head.next
            self.head.next = self.head.prev = None
        else:
            self.head = self.head.next
            self.head.prev = Node.prev
            self.head.prev.next = self.head
        return Node.element

def built_simple_binary_tree(lst:list) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()
    OurQueue = DoubleLL()
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
    def diameterOfBinaryTree1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def maxpath(root, MaxPath=0):
            if not root:
                return (0, MaxPath)
            left, leftmax = maxpath(root.left, MaxPath)
            right, rightmax = maxpath(root.right, MaxPath)
            MaxPath = max(MaxPath, left + right, leftmax, rightmax)
            return (1 + max(left, right), MaxPath)
        return maxpath(root, MaxPath=0)[1]

    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        OurStack = DoubleLL()
        OurDict = dict()
        OurStack.append((root, False))
        MaxPath = 0
        while OurStack.head:
            tempNode, Flag = OurStack.pop()
            if not Flag:
                OurStack.append((tempNode, True))
                if tempNode.left: OurStack.append((tempNode.left, False))
                if tempNode.right: OurStack.append((tempNode.right, False))
            else:
                if not tempNode.left and not tempNode.right:
                    OurDict[tempNode] = 1
                else:
                    leftPath = OurDict.get(tempNode.left, 0)
                    rightPath = OurDict.get(tempNode.right, 0)
                    MaxPath = max(MaxPath, (leftPath + rightPath))
                    OurDict[tempNode] = 1 + max(leftPath, rightPath)

        return MaxPath

    def diameterOfBinaryTree3(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        OurStack = deque()
        OurDict = dict()
        OurStack.append((root, False))
        MaxPath = 0
        while OurStack:
            tempNode, Flag = OurStack.pop()
            if not Flag:
                OurStack.append((tempNode, True))
                if tempNode.left: OurStack.append((tempNode.left, False))
                if tempNode.right: OurStack.append((tempNode.right, False))
            else:
                leftPath = OurDict.get(tempNode.left, 0)
                rightPath = OurDict.get(tempNode.right, 0)
                MaxPath = max(MaxPath, (leftPath + rightPath))
                OurDict[tempNode] = 1 + max(leftPath, rightPath)
        return MaxPath


root = [4,-7,-3,"null","null",-9,-3,9,-7,-4,"null",6,"null",-6,-6,"null","null",0,6,5,"null",9,"null","null",-1,-4,"null","null","null",-2]
# root = [1,2,3,4,5]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.diameterOfBinaryTree3(OurRoot))




