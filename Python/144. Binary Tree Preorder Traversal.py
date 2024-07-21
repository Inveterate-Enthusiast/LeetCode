# Given the root of a binary tree, return the preorder traversal of its nodes' values.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class DoublyLinkedListStack:
    head = None

    class Node:
        def __init__(self, element=None, next_node=None, prev_node=None):
            self.element = element
            self.next_node = next_node
            self.prev_node = prev_node

    def push(self, element):
        if not self.head:
            self.head = self.Node(element=element)
        elif not self.head.next_node:
            self.head.next_node = self.head.prev_node = self.Node(element=element, next_node=self.head, prev_node=self.head)
        else:
            self.head.prev_node.next_node = self.Node(element=element, next_node=self.head, prev_node=self.head.prev_node)
            self.head.prev_node = self.head.prev_node.next_node

    def pop(self):
        if not self.head:
            return None
        elif not self.head.next_node:
            Node = self.head
            self.head = self.head.next_node
        else:
            Node = self.head.prev_node
            if not self.head.prev_node.prev_node is self.head:
                self.head.prev_node = self.head.prev_node.prev_node
                self.head.prev_node.next_node = self.head
            else:
                self.head.next_node = self.head.prev_node = None
        return Node.element

def preorderTraversal1(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    OurList = []
    OurStack = []
    tempNode = root
    while tempNode or OurStack:
        while tempNode:
            OurList.append(tempNode.val)
            if tempNode.right: OurStack.append(tempNode)
            tempNode = tempNode.left


        if OurStack: tempNode = OurStack.pop()
        if tempNode: tempNode = tempNode.right

    return OurList

def preorderTraversal2(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    OurStack = [root]
    OurList = []

    while OurStack:
        curNode = OurStack.pop()
        OurList.append(curNode.val)

        if curNode.right:
            OurStack.append(curNode.right)
        if curNode.left:
            OurStack.append(curNode.left)
    return OurList

def inorderTraversal1(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    OurStack = []
    OurList = []
    curNode = root
    while curNode or OurStack:
        while curNode:
            OurStack.append(curNode)
            curNode = curNode.left

        curNode = OurStack.pop()
        OurList.append(curNode.val)
        curNode = curNode.right

    return OurList

class Solution:
    def preorderTraversal1(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        tempNode = root
        OurStack = DoublyLinkedListStack()
        OurStack.push(tempNode)
        OurList = []
        while OurStack.head:
            tempNode = OurStack.pop()
            OurList.append(tempNode.val)
            if tempNode.right: OurStack.push(tempNode.right)
            if tempNode.left: OurStack.push(tempNode.left)
        return OurList

    def preorderTraversal2(self, root: Optional[TreeNode]) -> list[int]:
        OurStack = DoublyLinkedListStack()
        OurStack.push(root)
        OurList = []
        while OurStack.head:
            tempNode = OurStack.pop()
            OurList.append(tempNode.val)
            if tempNode.right:
                OurStack.push(tempNode.right)
            if tempNode.left:
                OurStack.push(tempNode.left)

        return OurList


root = [6,4,9,2,5,8,12,1,3,'null','null',7,'null',10,14]
OurRoot = build_simple_binary_tree(root)
print(preorderTraversal2(OurRoot))
print(inorderTraversal1(OurRoot))

X = Solution()
print(X.preorderTraversal2(OurRoot))






