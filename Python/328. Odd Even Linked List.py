# Given the head of a singly linked list, group all the nodes
# with odd indices together followed by the nodes with even indices, and return the reordered list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
#
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_LinkedList(lst:list) -> Optional[ListNode]:
    OurNode = ListNode()
    tempNode = OurNode
    for x in lst:
        tempNode.next = ListNode(val=x)
        tempNode = tempNode.next
    else:
        OurNode = OurNode.next
    return OurNode

def oddEvenList1(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next or not head.next.next:
        return head
    firstNode = head
    secondNode = head.next
    evenNode = secondNode

    while firstNode.next and secondNode.next:
        firstNode.next = secondNode.next if secondNode.next else evenNode
        secondNode.next = secondNode.next.next if secondNode.next else None
        firstNode = firstNode.next
        secondNode = secondNode.next
    else:
        firstNode.next = evenNode
    return head

head = [1,2,3,4]
OurHead = build_LinkedList(head)
print(oddEvenList1(OurHead))










