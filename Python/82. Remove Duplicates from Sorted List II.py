# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list. Return the linked list sorted as well.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates1(head: Optional[ListNode]) -> Optional[ListNode]:
    OurFlag = False
    while head and head.next and head.val == head.next.val:
        head = head.next
        OurFlag = True
    else:
        if head and OurFlag:
            head = head.next
            OurFlag = False

    leftNode = rightNode = head
    while rightNode:
        if leftNode == rightNode:
            rightNode = rightNode.next
            continue
        elif leftNode.val == rightNode.val:
            while rightNode and rightNode.next and rightNode.val == rightNode.next.val:
                rightNode = rightNode.next
            else:
                leftNode = rightNode = head = rightNode.next
                continue


        while rightNode and rightNode.next and rightNode.val == rightNode.next.val:
            rightNode = rightNode.next
            OurFlag = True
        else:
            if rightNode and rightNode.next and OurFlag:
                rightNode = rightNode.next
                OurFlag = False
            elif rightNode and rightNode.next:
                leftNode.next = rightNode
                leftNode = rightNode
                rightNode = rightNode.next
            else:
                if leftNode: leftNode.next = rightNode.next if OurFlag else rightNode
                if rightNode: rightNode = rightNode.next

    return head


head = [1,1,1,2,2,2,3,3]
OurLinkedList = ListNode()
tempNode = OurLinkedList
for item in head:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList = OurLinkedList.next

tempNode = OurLinkedList
while tempNode.next:
    print(tempNode.val, "->", sep=" ", end=" ")
    tempNode = tempNode.next
else:
    print(tempNode.val, end="\n")

A = deleteDuplicates1(OurLinkedList)


while A.next:
    print(A.val, "->", sep=" ", end=" ")
    A = A.next
else:
    print(A.val, end="\n")