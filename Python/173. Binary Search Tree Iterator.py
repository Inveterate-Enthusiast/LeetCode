# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
#
# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
# The root of the BST is given as part of the constructor.
# The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
#
# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built_simple_binary_tree(lst:list) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()

    OurQueue = deque()
    rootNode = TreeNode(val=lst[0])
    OurQueue.append(rootNode)
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

    return rootNode

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.inorderList = deque()
        OurStack = deque()
        tempNode = self.root
        while tempNode or OurStack:
            while tempNode:
                OurStack.append(tempNode)
                tempNode = tempNode.left
            tempNode = OurStack.pop()
            self.inorderList.append(tempNode.val)
            tempNode = tempNode.right
        self.pointer = self.inorderList[0] - 1


    def next(self) -> int:
        assert len(self.inorderList) > 0, "This method isn't valid"
        if self.inorderList:
            if self.pointer < self.inorderList[0]:
                self.pointer = self.inorderList.popleft()
        return self.pointer

    def hasNext(self) -> bool:
        return len(self.inorderList) > 0


root = [7, 3, 15, "null", "null", 9, 20]
OurRoot = built_simple_binary_tree(root)

obj = BSTIterator(OurRoot)
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())













