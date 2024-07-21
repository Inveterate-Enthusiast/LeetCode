# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.

import math
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode1(head: Optional[ListNode]) -> Optional[ListNode]:
    OurLen = 0
    tempNode = head
    while tempNode:
        OurLen += 1
        tempNode = tempNode.next
    OurIndex = math.trunc(OurLen/2)+1
    tempNode = head
    for i in range(1, OurIndex):
        tempNode = tempNode.next

    return tempNode


def middleNode2(head: Optional[ListNode]) -> Optional[ListNode]:
    OurLen = 1
    index = 0
    tempNode = head
    while head:
        while ((math.trunc(OurLen/2)+1) - (index+1)) != 0:
            tempNode = tempNode.next
            index += 1
        head = head.next
        OurLen += 1
    return tempNode

head = [1,2,3,4,5]
OurLinkedList = ListNode()
tempNode = OurLinkedList
for item in head:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList = OurLinkedList.next

A = middleNode2(OurLinkedList)

while A.next:
    print(A.val, "->", sep=" ", end=" ")
    A = A.next
else:
    print(A.val, end="\n")