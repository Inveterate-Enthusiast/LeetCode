# Given the root of a binary tree, return the sum of every tree node's tilt.
#
# The tilt of a tree node is the absolute difference between the sum of all left subtree node values
# and all right subtree node values.
# If a node does not have a left child, then the sum of the left subtree node values is treated as 0.
# The rule is similar if the node does not have a right child.
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
    def findTilt1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        OurStack1 = DoubleLL()
        OurStack2 = DoubleLL()
        OurStack1.append(root)
        while OurStack1.head:
            tempNode = OurStack1.pop()
            tempNode.tilt = None
            tempNode.sum = None
            OurStack2.append(tempNode)
            if not tempNode.left and not tempNode.right:
                tempNode.tilt = 0
                tempNode.sum = tempNode.val
                continue
            if tempNode.left:
                OurStack1.append(tempNode.left)
            if tempNode.right:
                OurStack1.append(tempNode.right)

        OurSum = 0
        while OurStack2.head:
            tempNode = OurStack2.pop()
            if tempNode.tilt is None or tempNode.sum is None:
                tempNode.tilt = abs((tempNode.left.sum if tempNode.left else 0) - (tempNode.right.sum if tempNode.right else 0))
                OurSum += tempNode.tilt
                tempNode.sum = tempNode.val + ((tempNode.left.sum if tempNode.left else 0) + (tempNode.right.sum if tempNode.right else 0))
        return OurSum

    def findTilt2(self, root: Optional[TreeNode]) -> int:
        self.OurResult = 0

        def currentTilt(curNode) -> int:
            if not curNode:
                return 0
            leftSum = currentTilt(curNode.left)
            rightSum = currentTilt(curNode.right)
            curTilt = abs(leftSum - rightSum)
            self.OurResult += curTilt
            return sum([curNode.val, leftSum, rightSum])

        currentTilt(root)
        return self.OurResult


root = [4,2,9,3,5,"null",7]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.findTilt2(OurRoot))








