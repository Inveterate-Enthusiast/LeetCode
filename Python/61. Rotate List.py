# Given the head of a linked list, rotate the list to the right by k places.
# Циклический сдвиг k-раз

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight1(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return head

    OurLen = 0
    tempNode = head
    while tempNode:
        OurLen += 1
        tempNode = tempNode.next

    if k >= OurLen:
        k = k%OurLen

    if k == 0:
        return head

    leftNode = rightNode = tempNode = head
    for _ in range(k):
        rightNode = rightNode.next
    while rightNode.next:
        rightNode = rightNode.next
        leftNode = leftNode.next
    else:
        head = leftNode.next
        rightNode.next = tempNode
        leftNode.next = None

    return head

head = [1,2]; k = 1

OurLinkedList = ListNode()
tempNode = OurLinkedList
for item in head:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList = OurLinkedList.next

tempNode = OurLinkedList
while tempNode.next:
    print(tempNode.val, "->", sep=" ", end=" ")
    tempNode = tempNode.next
else:
    print(tempNode.val, end="\n")

A = rotateRight1(OurLinkedList, k)
while A.next:
    print(A.val, "->", sep=" ", end=" ")
    A = A.next
else:
    print(A.val, end="\n")