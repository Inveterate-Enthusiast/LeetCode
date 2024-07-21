# Given the root of a binary tree, return the inorder traversal of its nodes' values.


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DoublyNode:
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

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
            if self.head.prev_node.prev_node is self.head:
                self.head.next_node = self.head.prev_node = None
            else:
                self.head.prev_node = self.head.prev_node.prev_node
                self.head.prev_node.next_node = self.head
        return Node.element

def inorderTraversal1(root: Optional[TreeNode]) -> list[int]: # с помощью стека из массива
    OurList = []
    tempNode = root
    OurStack = []
    while OurStack or tempNode:
        while tempNode:
            OurStack.append(tempNode)
            tempNode = tempNode.left

        tempNode = OurStack.pop()
        if tempNode.val != "null": OurList.append(tempNode.val)
        tempNode = tempNode.right

    return OurList



def inorderTraversal2(root: Optional[TreeNode]) -> list[int]: # с помощью стека из двусвязного списка
    OurList = []
    OurStackHead = DoublyNode()
    tempTreeNode = root
    while OurStackHead.val or tempTreeNode:
        while tempTreeNode:
            if OurStackHead.val is None:
                OurStackHead.val = tempTreeNode
            elif OurStackHead.right is None:
                OurStackHead.right = OurStackHead.left = DoublyNode(val=tempTreeNode, right=OurStackHead, left=OurStackHead)
            else:
                OurStackHead.left.right = DoublyNode(tempTreeNode, OurStackHead, OurStackHead.left)
                OurStackHead.left = OurStackHead.left.right
            tempTreeNode = tempTreeNode.left

        if OurStackHead.right:
            tempTreeNode = OurStackHead.left.val
            OurStackHead.left = OurStackHead.left.left
            OurStackHead.left.right = None
        else:
            tempTreeNode = OurStackHead.val
            OurStackHead = DoublyNode()

        if tempTreeNode.val != "null": OurList.append(tempTreeNode.val)
        tempTreeNode  = tempTreeNode.right

    return OurList


def build_simple_binary_tree(root:list):
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

class Solution:
    def inorderTraversal1(self, root: Optional[TreeNode]) -> list[int]:
        tempNode = root
        OurStack = DoublyLinkedListStack()
        OurList = []
        while OurStack.head or tempNode:
            while tempNode:
                OurStack.push(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            OurList.append(tempNode.val)
            tempNode = tempNode.right
        return OurList

    def inorderTraversal2(self, root: Optional[TreeNode]) -> list[int]:
        OurStack = DoublyLinkedListStack()
        tempNode = root
        OurList = []
        while OurStack.head or tempNode:
            while tempNode:
                OurStack.push(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            OurList.append(tempNode.val)
            tempNode = tempNode.right
        return OurList






root = [2,3,"null",1]
OurRoot = build_simple_binary_tree(root)
X = Solution()

print(X.inorderTraversal2(OurRoot))