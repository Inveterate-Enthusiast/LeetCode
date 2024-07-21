# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_simple_binary_tree(root:list) -> Optional[TreeNode]:
    if not root:
        return TreeNode()

    OurQueue = deque()
    OurRoot = TreeNode(val=root[0])
    OurQueue.append(OurRoot)
    i = 1
    while i < len(root):
        tempNode = OurQueue.popleft()

        if i < len(root) and root[i] != "null":
            tempNode.left = TreeNode(val=root[i])
            OurQueue.append(tempNode.left)
        i += 1

        if i < len(root) and root[i] != "null":
            tempNode.right = TreeNode(val=root[i])
            OurQueue.append(tempNode.right)
        i += 1

    return OurRoot

class TwoWaysLinkedListStack:
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

class Solution:
    def leafSimilar1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        OurStack1 = TwoWaysLinkedListStack()
        OurStack2 = TwoWaysLinkedListStack()
        tempNode1 = root1; tempNode2 = root2
        while (OurStack1.head or tempNode1) or (OurStack2.head or tempNode2):
            while (OurStack1.head or tempNode1):
                while tempNode1:
                    OurStack1.push(tempNode1)
                    tempNode1 = tempNode1.left
                tempNode1 = OurStack1.pop()
                if not tempNode1 or (not tempNode1.left and not tempNode1.right):
                    break
                else:
                    tempNode1 = tempNode1.right

            while (OurStack2.head or tempNode2):
                while tempNode2:
                    OurStack2.push(tempNode2)
                    tempNode2 = tempNode2.left
                tempNode2 = OurStack2.pop()
                if not tempNode2 or (not tempNode2.left and not tempNode2.right):
                    break
                else:
                    tempNode2 = tempNode2.right

            if (tempNode1.val if tempNode1 else None) != (tempNode2.val if tempNode2 else None):
                return False
            else:
                tempNode1 = tempNode1.right if tempNode1 else None
                tempNode2 = tempNode2.right if tempNode2 else None

        return True

root1 = [3,5,1,6,7,4,2,"null","null","null","null","null","null",9,11,"null","null",8,10]; root2 = [3,5,1,6,2,9,8,"null","null",7,4]

OurRoot1 = build_simple_binary_tree(root1); OurRoot2 = build_simple_binary_tree(root2)
X = Solution()
print(X.leafSimilar1(OurRoot1, OurRoot2))















