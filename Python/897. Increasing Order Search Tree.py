# Given the root of a binary search tree,
# rearrange the tree in in-order so that the leftmost node
# in the tree is now the root of the tree, and every node has no left child and only one right child.
from typing import List, Optional
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
    def increasingBST1(self, root: TreeNode) -> TreeNode:
        OurStack = deque()
        OurQueue = deque()
        tempNode = root
        while OurStack or tempNode:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            OurQueue.append(tempNode)
            tempNode = tempNode.right

        newRoot = OurQueue.popleft()
        tempNode = newRoot
        while OurQueue:
            tempNode.left = None
            tempNode.right = OurQueue.popleft()
            tempNode = tempNode.right
        else:
            tempNode.left = tempNode.right = None
        return newRoot

root = [2,1,4,"null","null",3]
OurRoot = built_simple_binary_tree(root)
X = Solution()
Y = X.increasingBST1(OurRoot)
while Y.right:
    print(Y.val, end=" -> ")
    Y = Y.right
else:
    print(Y.val)












