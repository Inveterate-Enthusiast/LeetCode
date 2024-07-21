# You are given the head of a linked list of even length containing integers.
#
# Each odd-indexed node contains an odd integer and each even-indexed node contains an even integer.
#
# We call each even-indexed node and its next node a pair, e.g.,
# the nodes with indices 0 and 1 are a pair, the nodes with indices 2 and 3 are a pair, and so on.
#
# For every pair, we compare the values of the nodes in the pair:
#
# If the odd-indexed node is higher, the "Odd" team gets a point.
# If the even-indexed node is higher, the "Even" team gets a point.
# Return the name of the team with the higher points, if the points are equal, return "Tie".

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gameResult1(head: Optional[ListNode]) -> str:
    OurDict = {
        "Odd": 0,
        "Even":0
    }

    while head:
        if head.val > head.next.val:
            OurDict["Even"] += 1
        elif head.val < head.next.val:
            OurDict["Odd"] += 1
        head = head.next.next

    return "Tie" if OurDict["Odd"]==OurDict["Even"] else max(OurDict, key=lambda k: OurDict[k])

head = [1,2,10,1]
OurLinkedList = ListNode()
tempNode = OurLinkedList
for item in head:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList = OurLinkedList.next
print(gameResult1(OurLinkedList))