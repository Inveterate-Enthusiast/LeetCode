# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
from typing import Optional
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

class DoubleStack:
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
            if self.head.prev.prev is not self.head:
                self.head.prev = self.head.prev.prev
                self.head.prev.next = self.head
            else:
                self.head.next = self.head.prev = None
        return Node.element

class Solution:
    def binaryTreePaths1(self, root: Optional[TreeNode]) -> list[str]:
        OurList = []
        if not root:
            return OurList

        OurStack = DoubleStack()
        OurStack.append(element=(root, str(root.val)))
        while OurStack.head:
            tempNode, tempList = OurStack.pop()
            if not tempNode.left and not tempNode.right:
                OurList.append(tempList)
            if tempNode.left:
                OurStack.append((tempNode.left, tempList+"->"+str(tempNode.left.val)))
            if tempNode.right:
                OurStack.append((tempNode.right, tempList+"->"+str(tempNode.right.val)))
        return OurList

root = [1,2,3,"null",5]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.binaryTreePaths1(OurRoot))