# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TwoWaysLinkedList:
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
            if self.head.prev_node.prev_node is self.head:
                self.head.next_node = self.head.prev_node = None
            else:
                self.head.prev_node = self.head.prev_node.prev_node
                self.head.prev_node.next_node = self.head
        return (Node.element, Node.level)

def build_simple_binary_tree(root:list) -> Optional[TreeNode]:
    if not root:
        return TreeNode()

    OurQueue = []
    OurRoot = TreeNode(val=root[0])
    OurQueue.append(OurRoot)
    i = 1
    while i < len(root):
        curNode = OurQueue.pop(0)

        if i < len(root) and root[i] != "null":
            curNode.left = TreeNode(val=root[i])
            OurQueue.append(curNode.left)
        i += 1

        if i < len(root) and root[i] != "null":
            curNode.right = TreeNode(val=root[i])
            OurQueue.append(curNode.right)
        i += 1
    return OurRoot

def minDepth1(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    MinDeep = float("inf")
    OurStack = TwoWaysLinkedList()
    OurStack.append(element=root, level=1)

    while OurStack.head:
        curNode, curDeep = OurStack.pop()

        if curNode:
            if not curNode.left and not curNode.right:
                MinDeep = min(MinDeep, curDeep)
            else:
                if curNode.left: OurStack.append(element=curNode.left, level=curDeep+1)
                if curNode.right: OurStack.append(element=curNode.right, level=curDeep+1)

    return MinDeep

def minDepth2(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    OurStack = [(root, 1)]
    MinDeep = float("inf")

    while OurStack:
        curNode, curDeep = OurStack.pop()
        if curNode:
            if not curNode.left and not curNode.right:
                MinDeep = min(MinDeep, curDeep)
            else:
                if curNode.left: OurStack.append((curNode.left, 1 + curDeep))
                if curNode.right: OurStack.append((curNode.right, 1 + curDeep))

    return MinDeep

def minDepth3(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    oneDeep = minDepth3(root.left)
    twoDeep = minDepth3(root.right)
    return min((1 + oneDeep) if oneDeep else (twoDeep+1), (1 + twoDeep) if twoDeep else (oneDeep+1))





root = [2,"null",3,"null",4,"null",5,"null",6]
OurRoot = build_simple_binary_tree(root)
print(minDepth3(OurRoot))













