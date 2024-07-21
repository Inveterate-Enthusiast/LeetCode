# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
from typing import List, Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def built(lst: list) -> Optional[ListNode]:
    if not lst:
        return ListNode()

    root = ListNode(val=lst[0])
    tempNode = root
    i = 1
    while i < len(lst):
        tempNode.next = ListNode(val=lst[i])
        tempNode = tempNode.next
        i += 1

    return root

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lastNode = head; lastNode.past = None
        midNode = head
        step = 1
        while lastNode.next:
            step += 1
            if step%2:
                midNode = midNode.next

            lastNode.next.past = lastNode
            lastNode = lastNode.next

        nextLeftNode, nextRightNode = head, lastNode
        while nextLeftNode != midNode and nextRightNode != midNode:
            curLeftNode, curRightNode = nextLeftNode, nextRightNode
            nextLeftNode, nextRightNode = nextLeftNode.next, nextRightNode.past
            curLeftNode.next, curRightNode.next = curRightNode, nextLeftNode
        else:
            if step%2:
                midNode.next = None
            else:
                midNode.next.next = None




head = [1,2,3,4]
OurHead = built(head)
X = Solution()
X.reorderList(OurHead)

while OurHead.next:
    print(OurHead.val, end=" -> ")
    OurHead = OurHead.next
else:
    print(OurHead.val)

