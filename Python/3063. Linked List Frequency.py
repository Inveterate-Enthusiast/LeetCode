# Given the head of a linked list containing k distinct elements, return the head to a linked list of length k containing the
# frequency of each distinct element in the given linked list in any order.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def frequenciesOfElements1(head: Optional[ListNode]) -> Optional[ListNode]:
    OurDict = {}
    while head:
        OurDict[head.val] = OurDict.get(head.val, 0) + 1
        head = head.next

    OurLL = ListNode()
    tempNode = OurLL
    for value in OurDict.values():
        tempNode.next = ListNode(value)
        tempNode = tempNode.next
    else:
        OurLL = OurLL.next

    return OurLL

head = []
OurLinkedList = ListNode()
tempNode = OurLinkedList
for item in head:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList = OurLinkedList.next

A = frequenciesOfElements1(OurLinkedList)

while A.next:
    print(A.val, "->", sep=" ", end=" ")
    A = A.next
else:
    print(A.val, end="\n")