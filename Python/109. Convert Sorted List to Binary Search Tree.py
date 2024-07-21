# Given the head of a singly linked list where elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
from typing import Optional, List
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built_Linked_List(lst:list) -> Optional[ListNode]:
    if not lst:
        return ListNode()
    headNode = TreeNode()
    tempNode = headNode
    for x in lst:
        tempNode.next = ListNode(val=x)
        tempNode = tempNode.next
    else:
        headNode = headNode.next
    return headNode

class Solution:
    def sortedListToBST1(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        OurList = []
        tempNode = head
        while tempNode:
            OurList.append(tempNode.val)
            tempNode = tempNode.next

        def built_BST(lst:list) -> Optional[TreeNode]:
            if not lst:
                return None
            index = len(lst)//2
            return TreeNode(val=lst[index], left=built_BST(lst[:index]), right=built_BST(lst[index+1:]))

        return built_BST(OurList)

    def sortedListToBST2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        elif not head.next:
            return TreeNode(val=head.val)
        middleListNode = self.getMiddleNode(head)
        rootNode = TreeNode(val=middleListNode.val)
        rootNode.right = self.sortedListToBST2(middleListNode.next)
        middleListNode.next = None
        rootNode.left = self.sortedListToBST2(head)
        return rootNode

    def getMiddleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head
        prev = None
        while right and right.next:
            right = right.next.next
            prev = left
            left = left.next
        if prev: prev.next = None
        return left

    def sortedListToBST3(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        elif not head.next:
            return TreeNode(val=head.val)

        left = right = head
        prev = None
        while right and right.next:
            right = right.next.next
            prev = left
            left = left.next
        if prev: prev.next = None

        rootNode = TreeNode(val=left.val)
        rootNode.right = self.sortedListToBST3(left.next)
        rootNode.left = self.sortedListToBST3(head)
        return rootNode

    def sortedListToBST4(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(val=head.val)

        OurList = []
        tempNode = head
        while tempNode:
            OurList.append(tempNode.val)
            tempNode = tempNode.next

        OurStack = deque()
        OurStack.append((0, len(OurList)-1, None, None))
        OurRoot = None

        while OurStack:
            leftIndex, rightIndex, parentNode, leftFlag = OurStack.pop()

            if leftIndex > rightIndex:
                continue

            midIndex = (leftIndex + rightIndex)//2
            tempNode = TreeNode(val=OurList[midIndex])
            if not OurRoot: OurRoot = tempNode

            if parentNode:
                if leftFlag: parentNode.left = tempNode
                if not leftFlag: parentNode.right = tempNode

            OurStack.append((leftIndex, midIndex-1, tempNode, True))
            OurStack.append((midIndex+1, rightIndex, tempNode, False))
        return OurRoot

    def sortedListToBST5(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(val=head.val)

        OurList = []
        tempNode = head
        while tempNode:
            OurList.append(tempNode.val)
            tempNode = tempNode.next

        OurStack = deque()
        OurStack.append((0, len(OurList)-1, None, None))
        OurRoot = None
        while OurStack:
            leftIndex, rightIndex, curParent, Flag = OurStack.pop()

            if leftIndex > rightIndex:
                continue

            midIndex = (leftIndex + rightIndex) // 2
            tempNode = TreeNode(val=OurList[midIndex])
            if not OurRoot: OurRoot = tempNode

            if Flag:
                if Flag == "left": curParent.left = tempNode
                if Flag == "right": curParent.right = tempNode

            OurStack.append((leftIndex, midIndex-1, tempNode, "left"))
            OurStack.append((midIndex+1, rightIndex, tempNode, "right"))

        return OurRoot

    def sortedListToBST6(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(val=head.val)

        left = right = head
        prev = None
        while right and right.next:
            right = right.next.next
            prev = left
            left = left.next
        if prev: prev.next = None

        rootNode = TreeNode(val=left.val)
        rootNode.left = self.sortedListToBST6(head)
        rootNode.right = self.sortedListToBST6(left.next)
        return rootNode

    def sortedListToBST7(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        elif not head.next:
            return TreeNode(val=head.val)

        left = right = head
        prev = None
        while right and right.next:
            right = right.next.next
            prev = left
            left = left.next
        if prev: prev.next = None

        rootNode = TreeNode(val=left.val)
        rootNode.left = self.sortedListToBST7(head)
        rootNode.right = self.sortedListToBST7(left.next)
        return rootNode

    def sortedListToBST8(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(val=head.val)

        OurList = []
        tempNode = head
        while tempNode:
            OurList.append(tempNode.val)
            tempNode = tempNode.next

        OurStack = deque()
        OurStack.append((0, len(OurList)-1, None, None))
        rootNode = None
        while OurStack:
            leftIndex, rightIndex, curParent, curFlag = OurStack.pop()

            if leftIndex > rightIndex:
                continue

            midIndex = (leftIndex + rightIndex) // 2
            tempNode = TreeNode(val = OurList[midIndex])
            if not rootNode: rootNode = tempNode

            if curParent:
                if curFlag == "left": curParent.left = tempNode
                if curFlag == "right": curParent.right = tempNode

            OurStack.append((leftIndex, midIndex-1, tempNode, "left"))
            OurStack.append((midIndex+1, rightIndex, tempNode, "right"))

        return rootNode






head = [1,2,3]
OurHead = built_Linked_List(head)
X = Solution()
print(X.sortedListToBST8(OurHead))



