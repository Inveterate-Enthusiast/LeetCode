# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# The most significant bit is at the head of the linked list.

import math
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue1(head: ListNode) -> int:
    OurBN = ""
    while head:
        OurBN += str(head.val)
        head = head.next

    OurNumber = i = 0
    for index in range(len(OurBN)-1, -1, -1):
        OurNumber += (int(OurBN[index]) * (2**i))
        i += 1

    return OurNumber

head = [1,0,1]
OurLinkedList = ListNode()
tempNode = OurLinkedList
for item in head:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList = OurLinkedList.next

print(getDecimalValue1(OurLinkedList))