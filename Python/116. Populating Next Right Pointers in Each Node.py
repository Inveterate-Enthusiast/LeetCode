# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def built_simple_binary_tree(lst:list) -> Optional[Node]:
    if not lst:
        return Node()

    OurQueue = deque()
    rootNode = Node(val=lst[0])
    OurQueue.append(rootNode)
    i = 1
    while i < len(lst):
        tempNode = OurQueue.popleft()

        if i < len(lst) and lst[i] != "null":
            tempNode.left = Node(val=lst[i])
            OurQueue.append(tempNode.left)
        i += 1

        if i < len(lst) and lst[i] != "null":
            tempNode.right = Node(val=lst[i])
            OurQueue.append(tempNode.right)
        i += 1

    return rootNode

class Solution:
    def connect1(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        OurQueue = deque()
        OurQueue.append(root)

        while OurQueue:
            curLength = len(OurQueue)
            for i in range(curLength):
                tempNode = OurQueue.popleft()
                if OurQueue and i != (curLength-1): tempNode.next = OurQueue[0]
                if tempNode.left: OurQueue.append(tempNode.left)
                if tempNode.right: OurQueue.append(tempNode.right)

        return root

    def connect2(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        if root.left:
            root.left.next = root.right
            if root.next: root.right.next = root.next.left

        self.connect2(root.left)
        self.connect2(root.right)

        return root

    def connect3(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        tempNode = root

        while tempNode.left:
            curHead = tempNode
            while curHead:
                curHead.left.next = curHead.right
                if curHead.next: curHead.right.next = curHead.next.left
                curHead = curHead.next
            tempNode = tempNode.left

        return root

    def connect4(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        if not root.left and not root.right:
            return root

        OurQueue = deque()
        OurQueue.append(root)
        while OurQueue:
            curLength = len(OurQueue)
            for i in range(curLength):
                tempNode = OurQueue.popleft()
                if i != curLength-1:
                    tempNode.next = OurQueue[0]

                if tempNode.left: OurQueue.append(tempNode.left)
                if tempNode.right: OurQueue.append(tempNode.right)

        return root

    def connect5(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        if not root.left and not root.right:
            return root

        root.left.next = root.right
        if root.next: root.right.next = root.next.left
        self.connect5(root.left); self.connect5(root.right)

        return root

    def connect6(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        if not root.left and not root.right:
            return root

        tempNode = root
        while tempNode:
            curRoot = tempNode
            while curRoot:
                if curRoot.left:
                    curRoot.left.next = curRoot.right
                    if curRoot.next: curRoot.right.next = curRoot.next.left
                curRoot = curRoot.next

            tempNode = tempNode.left
        return root



root = [1,2,3,4,5,6,7]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.connect5(OurRoot))





