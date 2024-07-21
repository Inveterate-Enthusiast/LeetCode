# You are given the head of a linked list and two integers m and n.
#
# Traverse the linked list and remove some nodes in the following way:
#
# Start with the head as the current node.
# Keep the first m nodes starting with the current node.
# Remove the next n nodes
# Keep repeating steps 2 and 3 until you reach the end of the list.
# Return the head of the modified list after removing the mentioned nodes.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNodes1(head: ListNode, m: int, n: int) -> ListNode:
    tempNode = 1
    while tempNode:
        for _ in range(m):
            if tempNode == 1:
                tempNode = head
            elif tempNode:
                tempNode = tempNode.next
            else:
                break
        for _ in range(n):
            if tempNode and tempNode.next:
                tempNode.next = tempNode.next.next
            else:
                break

    return head

head = [1,2,3,4,5,6,7,8,9,10,11,12,13]; m = 2; n = 3

OurLinkedList = ListNode()
tempNode = OurLinkedList
for item in head:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList = OurLinkedList.next

A = deleteNodes1(OurLinkedList, m, n)
while A.next:
    print(A.val, "->", sep=" ", end=" ")
    A = A.next
else:
    print(A.val, end="\n")
