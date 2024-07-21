# Given the root of a binary search tree and a target value,
# return the value in the BST that is closest to the target.
# If there are multiple answers, print the smallest.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built_simple_binary_tree(lst:list) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()

    OurRoot = TreeNode(val=lst[0])
    OurQueue = deque()
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

class DoubleQueue:
    head = None

    class Node:
        def __init__(self, element=None, next=None, prev=None):
            self.element = element
            self.next = next
            self.prev = prev

    def append(self, element):
        if not self.head:
            self.head = self.Node(element=element)
        elif not self.head.next:
            self.head.next = self.head.prev = self.Node(element=element, next=self.head, prev=self.head)
        else:
            self.head.prev.next = self.Node(element=element, next=self.head, prev=self.head.prev)
            self.head.prev = self.head.prev.next

    def popleft(self):
        if not self.head:
            return None
        elif not self.head.next:
            Node = self.head
            self.head = self.head.next
        else:
            Node = self.head
            if not self.head.prev.prev is self.head:
                self.head = self.head.next
                self.head.prev = Node.prev
                self.head.prev.next = self.head
            else:
                self.head = self.head.next
                self.head.next = self.head.prev = None
        return Node.element

class Solution:
    def closestValue1(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return None
        OurResult = root.val
        OurQueue = DoubleQueue()
        OurQueue.append(root)
        while OurQueue.head:
            tempNode = OurQueue.popleft()

            if (abs(target-tempNode.val)) < (abs(target-OurResult)):
                OurResult = tempNode.val
            elif (abs(target-tempNode.val)) == (abs(target-OurResult)):
                OurResult = OurResult if OurResult < tempNode.val else tempNode.val

            if tempNode.left: OurQueue.append(tempNode.left)
            if tempNode.right: OurQueue.append(tempNode.right)
        return OurResult

root = [4,2,5,1,3]; target = 3.5
OurRoot = built_simple_binary_tree(root)
X = Solution()
print(X.closestValue1(OurRoot, target))





