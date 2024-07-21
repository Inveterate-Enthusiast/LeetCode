# Given a non-empty special binary tree consisting of nodes
# with the non-negative value,
# where each node in this tree has exactly two or zero sub-node.
# If the node has two sub-nodes,
# then this node's value is the smaller value among its two sub-nodes.
# More formally, the property root.val = min(root.left.val, root.right.val) always holds.
#
# Given such a binary tree, you need to output the second minimum value
# in the set made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.
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
    def findSecondMinimumValue1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        OurQueue = deque()
        OurSet = set()
        OurQueue.append(root)
        while OurQueue:
            tempNode = OurQueue.popleft()
            OurSet.add(tempNode.val)
            if tempNode.left: OurQueue.append(tempNode.left)
            if tempNode.right: OurQueue.append(tempNode.right)
        OurList = list(OurSet)
        OurList.sort()
        for item in OurList:
            if item > root.val:
                return item
        return -1

    def findSecondMinimumValue2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        OurQueue = deque()
        OurMid = None
        OurQueue.append(root)
        while OurQueue:
            tempNode = OurQueue.popleft()
            if tempNode.val > root.val:
                if OurMid is None:
                    OurMid = tempNode.val
                else:
                    OurMid = min(OurMid, tempNode.val)
            if tempNode.left: OurQueue.append(tempNode.left)
            if tempNode.right: OurQueue.append(tempNode.right)
        return OurMid if OurMid is not None else -1

root = [2,2,5,"null","null",5,7]
OurRoot = built_simply_binary_tree(root)
X = Solution()
print(X.findSecondMinimumValue2(OurRoot))






