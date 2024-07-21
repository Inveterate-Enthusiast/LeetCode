# Given the root of a Binary Search Tree (BST),
# return the minimum difference between the values of any two different nodes in the tree.
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

class DoubleLL:
    head = None

    class Node:
        def __init__(self, element=None, next=None, prev=None):
            self.element = element
            self.next = next
            self.prev = prev

    def append(self, new_element):
        if not self.head:
            self.head = self.Node(element=new_element)
        elif not self.head.next:
            self.head.next = self.head.prev = self.Node(element=new_element, next=self.head, prev=self.head)
        else:
            self.head.prev.next = self.Node(element=new_element, next=self.head, prev=self.head.prev)
            self.head.prev = self.head.prev.next

    def pop(self):
        if not self.head:
            return None
        elif not self.head.next:
            Node = self.head
            self.head = self.head.next
        else:
            Node = self.head.prev
            if self.head.prev.prev is self.head:
                self.head.next = self.head.prev = None
            else:
                self.head.prev = self.head.prev.prev
                self.head.prev.next = self.head
        return Node.element

    def popleft(self):
        if not self.head:
            return None

        Node = self.head
        if not self.head.next:
            self.head = None
        else:
            if self.head.prev.prev is self.head:
                self.head = self.head.next
                self.head.next = self.head.prev = None
            else:
                self.head = self.head.next
                self.head.prev = Node.prev
                self.head.prev.next = self.head

        return Node.element

class Solution:
    def minDiffInBST1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        OurStack = deque()
        tempNode = root
        OurMinVal = float("inf")
        prevNode = None
        while OurStack or tempNode:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            if prevNode: OurMinVal = min(OurMinVal, tempNode.val - prevNode.val)
            prevNode = tempNode
            tempNode = tempNode.right
        return OurMinVal

root = [4,2,6,1,3]
OurRoot = built_simply_binary_tree(root)
X = Solution()
print(X.minDiffInBST1(OurRoot))








