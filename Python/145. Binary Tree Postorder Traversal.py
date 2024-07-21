# Given the root of a binary tree, return the postorder traversal of its nodes' values.

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

def postorderTraversal1(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    OurStack1 = [root]
    OurStack2 = []
    OurList = []

    while OurStack1:
        curNode = OurStack1.pop()
        OurStack2.append(curNode)

        if curNode.left: OurStack1.append(curNode.left)
        if curNode.right: OurStack1.append(curNode.right)

    while OurStack2:
        curNode = OurStack2.pop()
        OurList.append(curNode.val)


    return OurList

class Solution:
    def postorderTraversal1(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        OurList = []
        OurStack1 = DoublyLinkedListStack()
        OurStack2 = DoublyLinkedListStack()
        OurStack1.push(root)

        while OurStack1.head:
            tempNode = OurStack1.pop()
            OurStack2.push(tempNode)

            if tempNode.left: OurStack1.push(tempNode.left)
            if tempNode.right: OurStack1.push(tempNode.right)

        while OurStack2.head:
            OurList.append(OurStack2.pop().val)

        return OurList

    def postorderTraversal2(self, root: Optional[TreeNode]) -> list[int]:
        OurList = []
        OurStack = DoublyLinkedListStack()
        OurStack.push(root)
        OurSecondStack = DoublyLinkedListStack()
        while OurStack.head:
            tempNode = OurStack.pop()
            OurSecondStack.push(tempNode)
            if tempNode.left:
                OurStack.push(tempNode.left)
            if tempNode.right:
                OurStack.push(tempNode.right)

        while OurSecondStack.head:
            OurList.append(OurSecondStack.pop().val)

        return OurList

root = [1,"null",2,3]
OurRoot = build_simple_binary_tree(root)
X = Solution()
print(X.postorderTraversal2(OurRoot))









