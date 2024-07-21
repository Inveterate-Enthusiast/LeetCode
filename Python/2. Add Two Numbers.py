from typing import Optional

class ListNode1:
    head = None

    class Node:
        value = None
        nextNode = None
        def __init__(self, value, nextNode = None):
            self.value = value
            self.nextNode = nextNode

    def append(self, newValue):
        if not self.head:
            self.head = self.Node(newValue, nextNode = None)
        else:
            currentNode = self.head
            while currentNode.nextNode:
                currentNode = currentNode.nextNode
            currentNode.nextNode = self.Node(newValue, nextNode=None)

    def get(self, index = None):
        i = 0
        currentNode = self.head
        while ((i < index) if not index is None else False) and currentNode.nextNode:
            currentNode = currentNode.nextNode
            i += 1
        return currentNode.value

    def length(self):
        if not self.head:
            return 0
        count = 1
        currentNode = self.head
        while currentNode.nextNode:
            count += 1
            currentNode = currentNode.nextNode
        return count

    def print(self):
        if not self.head:
            print(False)
        else:
            currentNode = self.head
            while currentNode.nextNode:
                print(currentNode.value, str(" -> "), sep= " ", end= " ")
                currentNode = currentNode.nextNode
            else:
                print(currentNode.value, end= "\n")



def addTwoNumbers(l1: Optional[ListNode1], l2: Optional[ListNode1]) -> Optional[ListNode1]:
    OurNewNumberList = ListNode1()
    LengthL1 = l1.length()
    LengthL2 = l2.length()
    i = 0
    while i < (LengthL1 if LengthL1 > LengthL2 else l2.length()):
        if i == 0:
            digit = (((l1.get(i)) if LengthL1 != 0 else 0) + ((l2.get(i)) if LengthL2 != 0 else 0))%10
            remainder = (((l1.get(i)) if LengthL1 != 0 else 0) + ((l2.get(i)) if LengthL2 != 0 else 0))//10
            OurNewNumberList.append(digit)
        else:
            digit = (remainder + ((l1.get(i)) if i < LengthL1 else 0) + ((l2.get(i)) if i < LengthL2 else 0))%10
            remainder = (remainder + ((l1.get(i)) if i < LengthL1 else 0) + ((l2.get(i)) if i < LengthL2 else 0))//10
            OurNewNumberList.append(digit)
            if (i == (LengthL1-1 if LengthL1 >= LengthL2 else  LengthL2-1)) and remainder != 0:
                OurNewNumberList.append(remainder)
        i += 1
    return OurNewNumberList

L1, L2 = ListNode1(), ListNode1()
L1.append(1)
L1.append(2)
L1.append(3)

L2.append(9)




# N = addTwoNumbers(L1, L2)
# N.print()




# РЕАЛИЗАЦИЯ ЧЕРЕЗ ОБЫЧНЫЙ СПИСОК
# def addTwoNumbers(l1:list, l2:list) -> list:
#     OurNewNumberList = []
#     for index in range(len(l1) if len(l1) >= len(l2) else len(l2)):
#         if index == 0:
#             digit = (l1[index] + l2[index])%10
#             remainder = (l1[index] + l2[index])//10
#             OurNewNumberList.append(digit)
#         else:
#             digit = (remainder + (((l1[index]) if index <= len(l1)-1 else 0) + ((l2[index]) if index <= len(l2)-1 else 0)))%10
#             remainder = (remainder + (((l1[index]) if index <= len(l1)-1 else 0) + ((l2[index]) if index <= len(l2)-1 else 0)))//10
#             OurNewNumberList.append(digit)
#             if (index == len(l1)-1 if len(l1) >= len(l2) else len(l2)-1) and remainder != 0:
#                 OurNewNumberList.append(remainder)
#     return OurNewNumberList

# решение в условиях LeetCode

class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next = next

def addTwoNumbers1(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    OurNewNumberList = ListNode()
    link = OurNewNumberList
    remainder = 0
    while l1 or l2:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        link.next = ListNode((remainder + a + b) % 10)
        link = link.next
        remainder = (remainder + a + b) // 10
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if remainder != 0:
        link.next = ListNode(remainder)

    return OurNewNumberList.next


def addTwoNumbers2(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    OurNumStr1 = ""
    OurNumStr2 = ""
    while l1:
        OurNumStr1 += str(l1.val)
        l1 = l1.next
    else:
        OurNumStr1 = int(OurNumStr1[::-1])

    while l2:
        OurNumStr2 += str(l2.val)
        l2 = l2.next
    else:
        OurNumStr2 = int(OurNumStr2[::-1])

    OurResultLL = ListNode()
    tempNode = OurResultLL
    for digit in (str(OurNumStr1 + OurNumStr2)[::-1]):
        tempNode.next = ListNode(digit)
        tempNode = tempNode.next
    else:
        OurResultLL = OurResultLL.next
    return OurResultLL

def addTwoNumbers3(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    OurResultLL = ListNode()
    tempNode = OurResultLL
    digit = tempDigit = 0
    while l1 and l2:
        digit = (l1.val + l2.val + tempDigit)%10
        tempDigit = (l1.val + l2.val + tempDigit)//10
        tempNode.next = ListNode(digit)
        tempNode = tempNode.next
        l1 = l1.next
        l2 = l2.next
    else:
        OurResultLL = OurResultLL.next
        if not l1 and not l2 and tempDigit:
            tempNode.next = ListNode(tempDigit)
            return OurResultLL

    while l1:
        digit = (l1.val + tempDigit) % 10
        tempDigit = (l1.val + tempDigit) // 10
        tempNode.next = ListNode(digit)
        tempNode = tempNode.next
        l1 = l1.next
    else:
        if tempDigit:
            tempNode.next = ListNode(tempDigit)

    while l2:
        digit = (l2.val + tempDigit) % 10
        tempDigit = (l2.val + tempDigit) // 10
        tempNode.next = ListNode(digit)
        tempNode = tempNode.next
        l2 = l2.next
    else:
        if tempDigit:
            tempNode.next = ListNode(tempDigit)

    return OurResultLL


L1 = [2,4,3]
OurLinkedList1 = ListNode()
tempNode = OurLinkedList1
for item in L1:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList1 = OurLinkedList1.next

L2 = [5,6,4]
OurLinkedList2 = ListNode()
tempNode = OurLinkedList2
for item in L2:
    tempNode.next = ListNode(item)
    tempNode = tempNode.next
else:
    OurLinkedList2 = OurLinkedList2.next

M = addTwoNumbers3(OurLinkedList1, OurLinkedList2)

while M.next:
    print(M.val, end="")
    M = M.next
else:
    print(M.val)