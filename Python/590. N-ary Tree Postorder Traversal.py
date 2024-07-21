# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the null value (See examples)
from typing import Optional
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder1(self, root: 'Node') -> list[int]:
        if not root:
            return []
        OurStack1 = deque(); OurStack2 = deque()
        OurStack1.append(root)
        OurList = []
        while OurStack1:
            tempNode = OurStack1.pop()
            OurStack2.append(tempNode)

            if tempNode.children:
                for child in tempNode.children:
                    OurStack1.append(child)
        while OurStack2:
            OurList.append(OurStack2.pop().val)
        return OurList


root = Node(val=1)
child21 = Node(val=3)
child22 = Node(val=2)
child23 = Node(val=4)
root.children = [child21, child22, child23]
child31 = Node(val=5)
child32 = Node(val=6)
child21.children = [child31, child32]
X = Solution()
print(X.postorder1(root))








