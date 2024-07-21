# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates1(head: Optional[ListNode]) -> Optional[ListNode]:
    OurLinkedList = ListNode(None)
    tempLL = OurLinkedList
    while head:
        if tempLL.val == head.val:
            head = head.next
            tempLL.next = head
        else:
            tempLL.next = head
            tempLL = tempLL.next
            head = head.next

    return OurLinkedList.next


def deleteDuplicates2(head: Optional[ListNode]) -> Optional[ListNode]:
    OurLinkedList = ListNode(val=None)
    tempNode = OurLinkedList

    while head:
        if tempNode.val == head.val:
            head = head.next
            tempNode.next = head
        else:
            tempNode.next = head
            tempNode = tempNode.next
            head = head.next

    return OurLinkedList.next


head = [1,1,2,3,3]
OurLinkedList = ListNode()
tempLL = OurLinkedList

for item in head:
    tempLL.next = ListNode(item)
    tempLL = tempLL.next
else:
    OurLinkedList = OurLinkedList.next

A = deleteDuplicates2(OurLinkedList)
while A.next:
    print(A.val, "->", sep=" ", end=" ")
    A = A.next
else:
    print(A.val)