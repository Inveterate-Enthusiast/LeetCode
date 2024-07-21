# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
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
    def preorder1(self, root: 'Node') -> list[int]:
        if not root:
            return []
        OurStack = deque()
        OurStack.append(root)
        OurList = []
        while OurStack:
            tempNode = OurStack.pop()
            OurList.append(tempNode.val)
            if tempNode.children:
                for i in range(len(tempNode.children)-1, -1, -1):
                    OurStack.append(tempNode.children[i])
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
print(X.preorder1(root))






