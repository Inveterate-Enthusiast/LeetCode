# You are given two binary trees root1 and root2.
#
# Imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
# You need to merge the two trees into a new binary tree.
# The merge rule is that if two nodes overlap, then sum node values up
# as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
#
# Return the merged tree.
#
# Note: The merging process must start from the root nodes of both trees.
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
    def mergeTrees1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        elif not root1:
            return root2
        elif not root2:
            return root1

        OurStack1 = DoubleLL(); OurStack2 = DoubleLL()
        OurRoot = TreeNode(); OurGeneralStack = DoubleLL()
        OurStack1.append(root1); OurStack2.append(root2)
        OurGeneralStack.append(OurRoot)
        while OurGeneralStack.head:
            tempGeneralNode = OurGeneralStack.pop()
            tempNode1 = OurStack1.pop(); tempNode2 = OurStack2.pop()

            if tempNode1 or tempNode2:
                tempGeneralNode.val = (tempNode1.val if tempNode1 else 0) + (tempNode2.val if tempNode2 else 0)

            for attr in ["right", "left"]:
                attr1 = getattr(tempNode1, attr) if tempNode1 else None
                attr2 = getattr(tempNode2, attr) if tempNode2 else None
                if not attr1 and not attr2:
                    continue
                else:
                    OurStack1.append(attr1)
                    OurStack2.append(attr2)
                    setattr(tempGeneralNode, attr, TreeNode())
                    OurGeneralStack.append(getattr(tempGeneralNode, attr))

        return OurRoot

root1 = [1,3,2,5]; root2 = [2,1,3,"null",4,"null",7]
OurRoot1 = built_simply_binary_tree(root1); OurRoot2 = built_simply_binary_tree(root2)
X = Solution()
print(X.mergeTrees1(OurRoot1, OurRoot2))













