# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.

from typing import Optional

class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

def hasCycle1(head: Optional[ListNode]) -> bool:
    OurSet = set()
    i = 0
    while i == len(OurSet) and head:
        OurSet.add(head)
        head = head.next
        i += 1
    else:
        if not head:
            return False
        else:
            return True


def hasCycle2(head: Optional[ListNode]) -> bool:
    if not head:
        return False

    while head:
        if hasattr(head, "visited"):
            return True
        else:
            head.visited = True
            head = head.next

    return False

head = [3,2,0,-4]; pos = -1

OurLinkedList = ListNode()
tempNode = OurLinkedList
cicleNode = None
i = 0
for item in head:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
    if i == pos:
        cicleNode = tempNode
    i += 1
else:
    if cicleNode:
        tempNode.next = cicleNode
    OurLinkedList = OurLinkedList.next


print(hasCycle2(OurLinkedList))
