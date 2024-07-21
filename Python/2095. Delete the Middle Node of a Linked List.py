# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
#
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
# where ⌊x⌋ denotes the largest integer less than or equal to x.
#
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


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

def deleteMiddle1(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return None
    fastNode = slowNode = head
    pastNode = slowNode
    flag = False
    while fastNode.next:
        fastNode = fastNode.next

        if not flag:
            pastNode = slowNode
            slowNode = slowNode.next
            flag = True
        else:
            flag = False
    else:
        pastNode.next = slowNode.next

    return head

def deleteMiddle2(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return None
    slowNode = head
    fastNode = head.next.next
    while fastNode and fastNode.next:
        fastNode = fastNode.next.next
        slowNode = slowNode.next
    else:
        slowNode.next = slowNode.next.next
    return head

head = [1,2]
OurListHead = build_LinkedList(head)
print(deleteMiddle2(OurListHead))



















