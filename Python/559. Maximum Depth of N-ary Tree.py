# Given a n-ary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).

from typing import Optional
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

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
    def maxDepth1(self, root: 'Node') -> int:
        if not root:
            return 0
        OurQueue = DoubleLL()
        OurQueue.append((root, 1))
        MaxLevel = 1
        while OurQueue.head:
            tempNode, level = OurQueue.popleft()
            MaxLevel = max(MaxLevel, level)
            if tempNode.children:
                for child in tempNode.children:
                    OurQueue.append((child, level+1))
        return MaxLevel

    def maxDepth2(self, root: 'Node') -> int:
        if not root:
            return 0
        OurQueue = deque()
        OurQueue.append((root, 1))
        MaxLevel = 1
        while OurQueue:
            tempNode, level = OurQueue.popleft()
            MaxLevel = max(MaxLevel, level)
            if tempNode.children:
                for child in tempNode.children:
                    OurQueue.append((child, level+1))
        return MaxLevel

root = Node(val=1)
child21 = Node(val=3)
child22 = Node(val=2)
child23 = Node(val=4)
root.children = [child21, child22, child23]
child31 = Node(val=5)
child32 = Node(val = 6)
child31.children = [child31, child32]
X = Solution()
print(X.maxDepth2(root))








