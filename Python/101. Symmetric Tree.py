# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TwoWayLinkedList:
    head = None

    class Node:
        element1 = None
        element2 = None
        next_node = None
        prev_node = None
        def __init__(self, element1, element2, next_node=None, prev_node=None):
            self.element1 = element1
            self.element2 = element2
            self.next_node = next_node
            self.prev_node = prev_node

    def append(self, element1, element2):
        if not self.head:
            self.head = self.Node(element1, element2)
            pass
        elif not self.head.next_node:
            self.head.next_node = self.head.prev_node = self.Node(element1, element2, next_node=self.head,  prev_node=self.head)
        else:
            self.head.prev_node.next_node = self.Node(element1, element2, next_node=self.head, prev_node=self.head.prev_node)
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
                self.head.prev_node.next_node = None
            else:
                self.head.next_node = None
                self.head.prev_node = None
        return (Node.element1, Node.element2)




def isSymmetric1(root: Optional[TreeNode]) -> bool:
    if not root.left and not root.right:
        return True
    elif not root.left or not root.right:
        return False

    leftChild = root.left; rightChild = root.right
    OurStack = TwoWayLinkedList()
    while OurStack.head or (leftChild and rightChild):
        while leftChild and rightChild:
            OurStack.append(leftChild, rightChild)
            leftChild = leftChild.left
            rightChild = rightChild.right
        else:
            if (leftChild.val if leftChild else None) != (rightChild.val if rightChild else None):
                return False

        leftChild, rightChild = OurStack.pop()
        if leftChild.val != rightChild.val:
            return False

        leftChild = leftChild.right
        rightChild = rightChild.left

    else:
        if (leftChild.val if leftChild else None) != (rightChild.val if rightChild else None):
            return False
    return True



# метод построения просто бинарного дерева с равномерным распределением
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

root = [1,2,2,3,4,4,3]
OurTree = build_simple_binary_tree(root)

print(isSymmetric1(OurTree))


