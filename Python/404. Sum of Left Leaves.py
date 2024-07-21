# Given the root of a binary tree, return the sum of all left leaves.
#
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
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
    def sumOfLeftLeaves1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        OurQueue = DoubleLL()
        root.leftleaf = False
        OurQueue.append(root)
        OurResult = 0
        while OurQueue.head:
            tempNode = OurQueue.popleft()
            if not tempNode.left and not tempNode.right and tempNode.leftleaf:
                OurResult += tempNode.val
            if tempNode.left:
                tempNode.left.leftleaf = True
                OurQueue.append(tempNode.left)
            if tempNode.right:
                tempNode.right.leftleaf = False
                OurQueue.append(tempNode.right)
        return OurResult

    def sumOfLeftLeaves2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        OurQueue = DoubleLL()
        OurQueue.append(root)
        OurResult = 0
        while OurQueue.head:
            tempNode = OurQueue.popleft()
            if tempNode.left and not tempNode.left.left and not tempNode.left.right:
                OurResult += tempNode.left.val

            if tempNode.left: OurQueue.append(tempNode.left)
            if tempNode.right: OurQueue.append(tempNode.right)
        return OurResult

root = [3,9,20,"null","null",15,7]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.sumOfLeftLeaves2(OurRoot))




