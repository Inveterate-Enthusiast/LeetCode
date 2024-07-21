# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists1(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    OurGeneralList = ListNode()
    tempLL = OurGeneralList
    while list1 and list2:
        if list1.val < list2.val:
            tempLL.next = list1
            list1 = list1.next
        else:
            tempLL.next = list2
            list2 = list2.next
        tempLL = tempLL.next

    if list1:
        tempLL.next = list1
    else:
        tempLL.next = list2


    return OurGeneralList.next


def mergeTwoLists2(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    OurLinkedList = ListNode()
    tempNode = OurLinkedList
    while list1 and list2:
        if list1.val <= list2.val:
            tempNode.next = list1
            tempNode = tempNode.next
            list1 = list1.next
        else:
            tempNode.next = list2
            tempNode = tempNode.next
            list2 = list2.next

    while list1:
        tempNode.next = list1
        tempNode = tempNode.next
        list1 = list1.next

    while list2:
        tempNode.next = list2
        tempNode = tempNode.next
        list2 = list2.next

    return OurLinkedList.next

list1 = [1]; list2 = []

LS1 = ListNode()
LS2 = ListNode()

cur1 = LS1
cur2 = LS2

for item in list1:
    cur1.val = item
    cur1.next = ListNode()
    cur1 = cur1.next


for item in list2:
    cur2.val = item
    cur2.next = ListNode()
    cur2 = cur2.next

print(mergeTwoLists1(LS1, LS2))