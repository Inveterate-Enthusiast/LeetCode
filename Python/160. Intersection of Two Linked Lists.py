# Given the heads of two singly linked-lists headA and headB,
# return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
#
# For example, the following two linked lists begin to intersect at node c1:

# The test cases are generated such that there are no cycles anywhere in the entire linked structure.
#
# Note that the linked lists must retain their original structure after the function returns.
#
# Custom Judge:
#
# The inputs to the judge are given as follows (your program is not given these inputs):
#
# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program.
# If you correctly return the intersected node, then your solution will be accepted.

from typing import Optional

class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

def getIntersectionNode1(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    tempNodeA = headA
    tempNodeB = headB
    while tempNodeA or tempNodeB:
        if tempNodeA:
            if hasattr(tempNodeA, "visitedB"):
                return tempNodeA
            else:
                tempNodeA.visitedA = True
                tempNodeA = tempNodeA.next

        if tempNodeB:
            if hasattr(tempNodeB, "visitedA"):
                return tempNodeB
            else:
                tempNodeB.visitedB = True
                tempNodeB = tempNodeB.next
    else:
        return None


def getIntersectionNode1(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    OurSet = set()
    while headA:
        OurSet.add(headA)
        headA = headA.next

    while headB:
        if headB in OurSet:
            return headB
        else:
            headB = headB.next

    return None

intersectVal = 2; listA = [0,1,2,3]; listB = [1,2,3]; skipA = 2; skipB = 1

interNode = None

OurLinkedListA = ListNode()
tempNodeA = OurLinkedListA
i = 0
for item in listA:
    tempNodeA.next = ListNode(item)
    tempNodeA = tempNodeA.next
    if not intersectVal == 0 and i == skipA and tempNodeA.val == intersectVal:
        interNode = tempNodeA
    i += 1
else:
    OurLinkedListA = OurLinkedListA.next

OurLinkedListB = ListNode()
tempNodeB = OurLinkedListB
j = 0
for item in listB:
    if intersectVal != 0 and j == skipB and interNode:
        tempNodeB.next = interNode
        tempNodeB = tempNodeB.next
    else:
        if tempNodeB.next and tempNodeB.next.val == item:
            tempNodeB = tempNodeB.next
            continue
        else:
            tempNodeB.next = ListNode(item)
            tempNodeB = tempNodeB.next
    j += 1
else:
    OurLinkedListB = OurLinkedListB.next

print(getIntersectionNode1(OurLinkedListA, OurLinkedListB))
