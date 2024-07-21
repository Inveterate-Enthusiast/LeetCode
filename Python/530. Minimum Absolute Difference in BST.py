# Given the root of a Binary Search Tree (BST),
# return the minimum absolute difference between the values of any two different nodes in the tree.
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
    def getMinimumDifference1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        OurStack = DoubleLL()
        OurSortedList = DoubleLL()
        tempNode = root
        while OurStack.head or tempNode:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            OurSortedList.append(element=tempNode.val)
            tempNode = tempNode.right
        OurMinVal = None
        while OurSortedList.head.next:
            if OurMinVal is None:
                OurMinVal = OurSortedList.head.next.element - OurSortedList.head.element
            else:
                OurMinVal = min(OurMinVal, OurSortedList.head.next.element - OurSortedList.head.element)
            OurSortedList.popleft()
        return OurMinVal

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        OurStack = DoubleLL()
        tempNode = root
        OurMinVal = float("inf")
        prevNode = None
        while OurStack.head or tempNode:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            if prevNode: OurMinVal = min(OurMinVal, tempNode.val - prevNode.val)
            prevNode = tempNode
            tempNode = tempNode.right
        return OurMinVal


root = [236,104,701,"null",227,"null",911]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.getMinimumDifference2(OurRoot))





