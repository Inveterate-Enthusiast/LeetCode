# Given the head of a linked list, remove the nth node from the end of the list and return its head.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd1(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    OurLen = 0
    tempNode = head
    while tempNode:
        OurLen+=1
        tempNode = tempNode.next
    n = OurLen-n-1
    tempNode = head
    while tempNode and n>0:
        tempNode = tempNode.next
        n-=1
    else:
        if n == 0:
            tempNode.next = tempNode.next.next
        elif n == -1:
            head = head.next
    return head


def removeNthFromEnd2(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    tempNode = ListNode()
    tempNode.next = head
    leftNode = rightNode = tempNode

    for _ in range(n+1):
        leftNode = leftNode.next

    while leftNode:
        leftNode = leftNode.next
        rightNode = rightNode.next
    else:
        if rightNode == tempNode:
            head = head.next
        else:
            rightNode.next = rightNode.next.next

    return head

head = [1,2,3,4,5]; n = 5

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

A = removeNthFromEnd2(OurLinkedList, n)


while A.next:
    print(A.val, "->", sep=" ", end=" ")
    A = A.next
else:
    print(A.val, end="\n")