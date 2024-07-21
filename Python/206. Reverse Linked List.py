# Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList1(head: Optional[ListNode]) -> Optional[ListNode]:
    leftNode = None
    middleNode = rightNode = head
    while middleNode:
        rightNode = rightNode.next if rightNode else None
        middleNode.next = leftNode
        leftNode = middleNode
        middleNode = rightNode
    else:
        head = leftNode
    return head

def reverseList2(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    elif not head.next:
        return head
    lastNode = head
    leftNode = lastNode.next; lastNode.next = None
    rightNode = leftNode.next if leftNode else None
    while rightNode:
        leftNode.next = lastNode
        lastNode = leftNode
        leftNode = rightNode
        rightNode = rightNode.next
    else:
        leftNode.next = lastNode
        head = leftNode

    return head

def reverseList3(head: Optional[ListNode]) -> Optional[ListNode]:
    leftNode = None
    middleNode = rightNode = head

    while middleNode:
        rightNode = rightNode.next if rightNode else None
        middleNode.next = leftNode
        leftNode = middleNode; middleNode = rightNode
    else:
        head = leftNode
    return head

head = [1]
OurLinkedList = ListNode()
tempNode = OurLinkedList
for item in head:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList = OurLinkedList.next

A = reverseList2(OurLinkedList)
while A.next:
    print(A.val, "->", sep=" ", end=" ")
    A = A.next
else:
    print(A.val)