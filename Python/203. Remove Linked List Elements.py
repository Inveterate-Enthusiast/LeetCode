# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val, and return the new head.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements1(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    while head and head.val == val:
        head = head.next

    tempNode = head
    while tempNode:
        if tempNode.next and tempNode.next.val == val:
            tempNode.next = tempNode.next.next
        else:
            tempNode = tempNode.next
    return head

head = [1,2,2,1]; val = 2

OurLinkedList = ListNode()
tempNode = OurLinkedList
for item in head:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList = OurLinkedList.next

A = removeElements1(OurLinkedList, val)
while A.next:
    print(A.val, "->", sep=" ", end=" ")
    A = A.next
else:
    print(A.val)