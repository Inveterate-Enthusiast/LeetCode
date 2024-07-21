# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs1(head: Optional[ListNode]) -> Optional[ListNode]:
    tempNode = head
    leftNode = rightNode = tempNode
    while rightNode:
        if rightNode == leftNode:
            rightNode = rightNode.next
            continue
        if head == leftNode:
            head = rightNode
        if not rightNode.next:
            leftNode.next = rightNode.next
            rightNode.next = leftNode
            break
        leftNode.next = rightNode.next
        rightNode.next = leftNode
        rightNode = leftNode.next
        leftNode.next = rightNode.next if rightNode.next else leftNode.next
        leftNode = rightNode

    return head

head = [1,2]
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

A = swapPairs1(OurLinkedList)
while A.next:
    print(A.val, "->", sep=" ", end=" ")
    A = A.next
else:
    print(A.val, end="\n")