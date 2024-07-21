# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

from typing import Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TwoLinkedStack:
    head = None

    class Node:
        def __init__(self, element=None, left=None, right=None, next_node=None, prev_node=None):
            self.element = element
            self.left = left
            self.right = right
            self.next_node = next_node
            self.prev_node = prev_node

    def append(self, element, left, right):
        if not self.head:
            self.head = self.Node(element=element, left=left, right=right)
        elif not self.head.next_node:
            self.head.next_node = self.head.prev_node = self.Node(element=element, left=left, right=right, next_node=self.head, prev_node=self.head)
        else:
            self.head.prev_node.next_node = self.Node(element=element, left=left, right=right, next_node=self.head, prev_node=self.head.prev_node)
            self.head.prev_node = self.head.prev_node.next_node

    def pop(self):
        if not self.head:
            return (None, None, None)
        elif not self.head.next_node:
            Node = self.head
            self.head = self.head.next_node
        else:
            Node = self.head.prev_node
            if self.head.prev_node.prev_node is not self.head:
                self.head.prev_node = self.head.prev_node.prev_node
                self.head.prev_node.next_node = self.head
            else:
                self.head.next_node = self.head.prev_node = None
        return (Node.element, Node.left, Node.right)


def sortedArrayToBST1(nums: list[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return TreeNode(val=nums[0])

    i = (len(nums) // 2)
    OurTreeNode = TreeNode(val=nums[i])
    OurTreeNode.left = sortedArrayToBST1(nums[:i])
    OurTreeNode.right = sortedArrayToBST1(nums[i+1:])

    return OurTreeNode

def sortedArrayToBST2(nums: list[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    OurRoot = TreeNode() # создаем пустую вершину, которая будет корнем
    OurStack = [(OurRoot, 0, len(nums) - 1)] # используем стек для отслеживания узлов и их границ в массиве

    while OurStack:
        curNode, left, right = OurStack.pop()
        mid = left + (right-left) // 2 # находим середину текущего подмассива

        curNode.val = nums[mid] # присваиваем текущему узлу значение середину текущего подмассива

        if left <= (mid-1): # если есть левая часть подмассива
            curNode.left = TreeNode()
            OurStack.append((curNode.left, left, mid-1))

        if right >= (mid+1): # если есть правая часть подмассива
            curNode.right = TreeNode()
            OurStack.append((curNode.right, mid+1, right))

    return OurRoot

def sortedArrayToBST3(nums: list[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    OurRoot = TreeNode()
    OurStack = [(OurRoot, 0, len(nums)-1)]

    while OurStack:
        curNode, left, right = OurStack.pop()
        mid = left + (right - left)//2
        curNode.val = nums[mid]

        if left <= (mid-1):
            curNode.left = TreeNode()
            OurStack.append((curNode.left, left, mid-1))

        if right >= (mid+1):
            curNode.right = TreeNode()
            OurStack.append((curNode.right, mid+1, right))

    return OurRoot

def sortedArrayToBST4(nums: list[int]) -> Optional[TreeNode]: # через двусвязный список
    OurRoot = TreeNode()
    OurStack = TwoLinkedStack()
    OurStack.append(element=OurRoot, left=0, right=(len(nums)-1))

    while OurStack.head:
        curNode, left, right = OurStack.pop()
        mid = left + (right-left)//2
        curNode.val = nums[mid]

        if left < mid:
            curNode.left = TreeNode()
            OurStack.append(curNode.left, left, mid-1)

        if right > mid:
            curNode.right = TreeNode()
            OurStack.append(curNode.right, mid+1, right)

    return OurRoot




nums = [-10,-3,0,5,9]
print(sortedArrayToBST4(nums))