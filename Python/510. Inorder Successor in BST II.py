# Given a node in a binary search tree, return the in-order successor of that node in the BST.
# If that node has no in-order successor, return null.
#
# The successor of a node is the node with the smallest key greater than node.val.
#
# You will have direct access to the node but not to the root of the tree.
# Each node will have a reference to its parent node. Below is the definition for Node:
#
# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
from typing import List, Tuple, Optional
from collections import deque, defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def build(lst:list, nv:int) -> Optional[Node]:
    if not lst:
        return Node()
    OurQueue = deque()
    root = Node(val=lst[0])
    needNode = None
    OurQueue.append(root)
    i = 1
    while i < len(lst):
        curNode = OurQueue.popleft()
        if curNode.val == nv: needNode = curNode
        if i < len(lst) and lst[i] != "null":
            curNode.left = Node(val=lst[i])
            curNode.left.parent = curNode
            OurQueue.append(curNode.left)
        i += 1

        if i < len(lst) and lst[i] != "null":
            curNode.right = Node(val=lst[i])
            curNode.right.parent = curNode
            OurQueue.append(curNode.right)
        i += 1

    while not needNode and OurQueue:
        if (curNode := OurQueue.popleft()).val == nv:
            needNode = curNode
    return needNode

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        def findRoot(child: 'Node') -> 'Optional[Node]':
            if not child:
                return None
            elif not child.parent:
                return child
            return findRoot(child.parent)

        OurRoot = findRoot(node)

        OurStack = deque(); tempNode = OurRoot
        OurSuccessor = None; OurFlag = False
        while OurStack or tempNode:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            if OurFlag: OurSuccessor = (OurSuccessor if OurSuccessor.val <= tempNode.val else tempNode) if OurSuccessor else tempNode
            if tempNode is node: OurFlag = True
            tempNode = tempNode.right
        return OurSuccessor

    def inorderSuccessor1(self, node: 'Node') -> 'Optional[Node]':
        def findRoot(child: 'Node') -> 'Optional[Node]':
            if not child:
                return None
            elif not child.parent:
                return child
            return findRoot(child.parent)

        OurRoot = findRoot(node)

        OurStack = deque(); tempNode = OurRoot
        OurFlag = False
        while OurStack or tempNode:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            if OurFlag: return tempNode
            if tempNode is node: OurFlag = True
            tempNode = tempNode.right
        return None

    def inorderSuccessor2(self, node: 'Node') -> 'Optional[Node]':
        if not node:
            return None

        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        if node.parent:
            if node is node.parent.left:
                return node.parent

            elif node is node.parent.right:
                node = node.parent
                while node.parent and (node is node.parent.right):
                    node = node.parent
                return node.parent

        return None


tree = [5,3,6,2,4,"null","null",1]; node = 6
OurNode = build(tree, node)
X = Solution()
print(X.inorderSuccessor2(OurNode).val)
