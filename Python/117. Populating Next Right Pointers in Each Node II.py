# Given a binary tree
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
    def connect1(self, root: Node) -> Node:
        if not root:
            return None
        if not root.left and not root.right:
            return root

        OurQueue = deque()
        OurQueue.append(root)
        while OurQueue:
            curLen = len(OurQueue)
            for i in range(1, curLen+1):
                tempNode = OurQueue.popleft()
                if i != curLen:
                    tempNode.next = OurQueue[0]
                if tempNode.left: OurQueue.append(tempNode.left)
                if tempNode.right: OurQueue.append(tempNode.right)
        return root

    def connect2(self, root: Node) -> Node:
        if not root:
            return None
        if not root.left and not root.right:
            return root

        tempNode = root
        while tempNode:
            curRoot = tempNode
            curChild = None
            nextLevel = None
            while curRoot:
                if curRoot.left:
                    if curChild:
                        curChild.next = curRoot.left
                        curChild = curChild.next
                    else:
                        curChild = curRoot.left
                        if not nextLevel: nextLevel = curChild

                if curRoot.right:
                    if curChild:
                        curChild.next = curRoot.right
                        curChild = curChild.next
                    else:
                        curChild = curRoot.right
                        if not nextLevel: nextLevel = curChild
                curRoot = curRoot.next
            tempNode = nextLevel
        return root


root = [-9,-3,2,"null",4,4,0,-6,"null",-5]
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.connect2(OurRoot))








