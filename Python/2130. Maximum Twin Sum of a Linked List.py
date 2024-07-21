# In a linked list of size n, where n is even, the ith node (0-indexed)
# of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
#
# For example, if n = 4, then node 0 is the twin of node 3,
# and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
#
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

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

def pairSum1(head: Optional[ListNode]) -> int:
    if not head:
        return None

    OurStack = []; OurMaxSum = None
    leftNode = head
    rightNode = head.next.next
    while rightNode and rightNode.next:
        OurStack.append(leftNode.val)
        rightNode = rightNode.next.next
        leftNode = leftNode.next
    else:
        OurStack.append(leftNode.val)
        leftNode = leftNode.next

    while leftNode:
        OurMaxSum = (leftNode.val + OurStack.pop()) if OurMaxSum is None else max(OurMaxSum, (leftNode.val + OurStack.pop()))
        leftNode = leftNode.next

    return OurMaxSum

head = [5,4,2,1]
OurHead = build_LinkedList(head)
print(pairSum1(OurHead))






