# Given the roots of two binary trees root and subRoot,
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree
# and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DoubleLL:
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

    def pop(self):
        if not self.head:
            return None
        elif not self.head.next:
            Node = self.head
            self.head = self.head.next
        else:
            Node = self.head.prev
            if not self.head.prev.prev is self.head:
                self.head.prev = self.head.prev.prev
                self.head.prev.next = self.head
            else:
                self.head.next = self.head.prev = None
        return Node.element

    def popleft(self):
        if not self.head:
            return None
        Node = self.head
        if not self.head.next:
            self.head = self.head.next
        elif self.head.prev.prev is self.head:
            self.head = self.head.next
            self.head.next = self.head.prev = None
        else:
            self.head = self.head.next
            self.head.prev = Node.prev
            self.head.prev.next = self.head
        return Node.element

def built_simple_binary_tree(lst:list) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()
    OurQueue = DoubleLL()
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

class Solution:
    def isSubtree1(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not subRoot:
            return False
        elif not root:
            return False

        OurTempQueue = DoubleLL()
        OurTempQueue.append(root)
        OurGeneralQueue = DoubleLL()
        while OurTempQueue.head:
            tempNode = OurTempQueue.popleft()
            if tempNode.val == subRoot.val: OurGeneralQueue.append(tempNode)
            if tempNode.left: OurTempQueue.append(tempNode.left)
            if tempNode.right: OurTempQueue.append(tempNode.right)

        while OurGeneralQueue.head:
            tempNode = OurGeneralQueue.popleft()
            OurStack1 = DoubleLL(); OurStack2 = DoubleLL()
            OurStack1.append(tempNode); OurStack2.append(subRoot)
            while OurStack1.head and OurStack2.head:
                Node1 = OurStack1.pop(); Node2 = OurStack2.pop()
                if Node1.val != Node2.val:
                    break

                for nodeAttr in ["right", "left"]:
                    OurFlag = (getattr(Node1, nodeAttr) is not None) != (getattr(Node2, nodeAttr) is not None)
                    if OurFlag:
                        break
                    else:
                        if getattr(Node1, nodeAttr): OurStack1.append(getattr(Node1, nodeAttr))
                        if getattr(Node2, nodeAttr): OurStack2.append(getattr(Node2, nodeAttr))

                if not OurFlag and not OurStack1.head and not OurStack2.head:
                    return True
                elif OurFlag:
                    break
        return False

root = [3,4,5,1,2]; subRoot = [4,1,2,1]
OurRoot = built_simple_binary_tree(root); OurSubRoot = built_simple_binary_tree(subRoot)
X = Solution()
print(X.isSubtree1(OurRoot, OurSubRoot))











