#Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome1(head: Optional[ListNode]) -> bool:
    leftNode = None
    middleNode = ListNode(head.val)
    rightNode = head
    while middleNode:
        rightNode = rightNode.next if rightNode else None
        middleNode.next = leftNode
        leftNode = middleNode
        middleNode = ListNode(rightNode.val) if rightNode else None
    else:
        newHead = leftNode

    while head:
        if head.val != newHead.val:
            return False
        head = head.next
        newHead = newHead.next

    return True

def isPalindrome2(head: Optional[ListNode]) -> bool:
    OurStack = []
    tempNode = head
    while tempNode:
        OurStack.append(tempNode.val)
        tempNode = tempNode.next

    tempNode = head
    while tempNode:
        if tempNode.val != OurStack.pop():
            return False
        tempNode = tempNode.next

    return True


head = [1,2,2,1]
OurLinkedList = ListNode()
tempNode = OurLinkedList
for item in head:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList = OurLinkedList.next

print(isPalindrome1(OurLinkedList))
while OurLinkedList.next:
    print(OurLinkedList.val, "->", sep=" ", end=" ")
    OurLinkedList = OurLinkedList.next
else:
    print(OurLinkedList.val, end="\n")