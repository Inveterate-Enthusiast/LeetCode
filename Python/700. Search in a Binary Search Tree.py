# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val
# and return the subtree rooted with that node. If such a node does not exist, return null.
from typing import Optional
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
    def searchBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if not val:
            return None

        OurStack = deque()
        OurStack.append(root)
        while OurStack:
            tempNode = OurStack.pop()
            if tempNode.val == val:
                return tempNode
            if tempNode.val > val:
                if tempNode.left: OurStack.append(tempNode.left)
            elif tempNode.val < val:
                if tempNode.right: OurStack.append(tempNode.right)

        return None

    def searchBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        OurQueue = deque()
        OurQueue.append(root)
        while OurQueue:
            tempNode = OurQueue.popleft()
            if tempNode.val == val:
                return tempNode
            if tempNode.left: OurQueue.append(tempNode.left)
            if tempNode.right: OurQueue.append(tempNode.right)
        return None



root = [4,2,7,1,3]; val = 2
OurRoot = built_simply_binary_tree(root)
X = Solution()
print(X.searchBST2(OurRoot, val))





