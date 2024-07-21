# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TwoWayLinkedList:
    head = None

    class Node:
        def __init__(self, element=None, level=None, next_node=None, prev_node=None):
            self.element = element
            self.level = level
            self.next_node = next_node
            self.prev_node = prev_node

    def append(self, element, level):
        if not self.head:
            self.head = self.Node(element=element, level=level)
            pass
        elif not self.head.next_node:
            self.head.next_node = self.head.prev_node = self.Node(element=element, level=level, next_node=self.head, prev_node=self.head)
        else:
            self.head.prev_node.next_node = self.Node(element=element, level=level, next_node=self.head, prev_node=self.head.prev_node)
            self.head.prev_node = self.head.prev_node.next_node

    def pop(self):
        if not self.head:
            return (None, None)
        elif not self.head.next_node:
            Node = self.head
            self.head = self.head.next_node
        else:
            Node = self.head.prev_node
            if self.head.prev_node.prev_node is not self.head:
                self.head.prev_node = self.head.prev_node.prev_node
                self.head.prev_node.next_node = self.head
            else:
                self.head.next_node = self.head.prev_node = None
        return (Node.element, Node.level)

def built_simple_binary_tree(root:list) -> TreeNode:
    if not root:
        return None

    queue = []
    root_node = TreeNode(val=root[0])
    queue.append(root_node)
    i = 1
    while i < len(root):
        curNode = queue.pop(0)
        if i < len(root) and root[i] != "null":
            curNode.left = TreeNode(val=root[i])
            queue.append(curNode.left)
        i += 1
        if i < len(root) and root[i] != "null":
            curNode.right = TreeNode(val=root[i])
            queue.append(curNode.right)
        i += 1

    return root_node


def maxDepth1(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    OurCount = 0
    curCount = 1
    curNode = root
    OurStack = TwoWayLinkedList()
    while OurStack.head or curNode:
        while curNode:
            OurStack.append(curNode, curCount)
            curNode = curNode.left
            curCount += 1

        curNode, curCount = OurStack.pop()
        OurCount = max(OurCount, curCount)
        curNode = curNode.right
        curCount += 1

    return OurCount



def maxDepth2(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    MaxDeep = 0
    OurStack = TwoWayLinkedList()
    OurStack.append(element=root, level=1)
    while OurStack.head:
        curNode, curDeep = OurStack.pop()

        if curNode:
            MaxDeep = max(MaxDeep, curDeep)
            if curNode.left:
                OurStack.append(curNode.left, curDeep+1)
            if curNode.right:
                OurStack.append(curNode.right, curDeep+1)
    return MaxDeep


class Solution:
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        OurMaxDepth = 0; curDepth = 1
        OurStack = deque()
        tempNode = root
        while OurStack or tempNode:
            while tempNode:
                OurStack.append((tempNode, curDepth))
                tempNode = tempNode.left
                curDepth += 1

            tempNode, curDepth = OurStack.pop()
            OurMaxDepth = max(curDepth, OurMaxDepth)
            tempNode = tempNode.right; curDepth += 1

        return OurMaxDepth




root = [3,9,20,"null","null",15,7]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.maxDepth1(OurRoot))









