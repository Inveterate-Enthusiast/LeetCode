# Given the root of a binary tree,
# return the average value of the nodes on each level in the form of an array.
# Answers within 10-5 of the actual answer will be accepted.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built_simply_binary_tree(lst:list) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()

    OurQueue = deque()
    OurRoot = TreeNode(val=lst[0])
    OurQueue.append(OurRoot)
    i = 1
    while i < len(lst):
        tempNode = OurQueue.popleft()
        if i < len(lst) and lst[i] != "null":
            tempNode.left = TreeNode(val=lst[i])
            OurQueue.append(tempNode.left)
        i += 1

        if i < len(lst) and lst[i] != "null":
            tempNode.right = TreeNode(val=lst[i])
            OurQueue.append(tempNode.right)
        i += 1

    return OurRoot

class DoubleLL:
    head = None

    class Node:
        def __init__(self, element=None, next=None, prev=None):
            self.element = element
            self.next = next
            self.prev = prev

    def append(self, new_element):
        if not self.head:
            self.head = self.Node(element=new_element)
        elif not self.head.next:
            self.head.next = self.head.prev = self.Node(element=new_element, next=self.head, prev=self.head)
        else:
            self.head.prev.next = self.Node(element=new_element, next=self.head, prev=self.head.prev)
            self.head.prev = self.head.prev.next

    def pop(self):
        if not self.head:
            return None
        elif not self.head.next:
            Node = self.head
            self.head = self.head.next
        else:
            Node = self.head.prev
            if self.head.prev.prev is self.head:
                self.head.next = self.head.prev = None
            else:
                self.head.prev = self.head.prev.prev
                self.head.prev.next = self.head
        return Node.element

    def popleft(self):
        if not self.head:
            return None

        Node = self.head
        if not self.head.next:
            self.head = None
        else:
            if self.head.prev.prev is self.head:
                self.head = self.head.next
                self.head.next = self.head.prev = None
            else:
                self.head = self.head.next
                self.head.prev = Node.prev
                self.head.prev.next = self.head

        return Node.element

class Solution:
    def averageOfLevels1(self, root: Optional[TreeNode]) -> list[float]: # Depth-First-Search (inorder traversal)
        if not root:
            return []
        OurStack = DoubleLL()
        tempNode = root
        i = 0; OurDict = dict()
        while OurStack.head or tempNode:
            while tempNode:
                i += 1
                if OurDict.get(i, None):
                    OurDict[i].append(tempNode.val)
                else:
                    OurDict[i] = [tempNode.val]
                OurStack.append((tempNode, i))
                tempNode = tempNode.left
            tempNode, i = OurStack.pop()
            tempNode = tempNode.right

        OurList = []
        maxLevel = max(OurDict.keys())
        for j in range(1, maxLevel+1):
            OurList.append(sum(OurDict[j])/(len(OurDict[j])))

        return OurList

    def averageOfLevels2(self, root: Optional[TreeNode]) -> list[float]:
        if not root:
            return []
        OurQueue = deque()
        OurQueue.append(root)
        OurList = []
        while OurQueue:
            lenQueue = len(OurQueue)
            tempSum = 0
            for i in range(lenQueue):
                tempNode = OurQueue.popleft()
                tempSum += tempNode.val
                if tempNode.left: OurQueue.append(tempNode.left)
                if tempNode.right: OurQueue.append(tempNode.right)
            OurList.append(tempSum/lenQueue)
        return OurList

root = [3,9,20,"null","null",15,7]
OurRoot = built_simply_binary_tree(root)
X = Solution()
print(X.averageOfLevels2(OurRoot))











