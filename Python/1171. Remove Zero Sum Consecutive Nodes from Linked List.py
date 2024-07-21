#Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

#After doing so, return the head of the final linked list.  You may return any such answer.

#(Note that in the examples below, all sequences are serializations of ListNode objects.)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists1(head: ListNode) -> ListNode:
    OurDummy = ListNode(0)
    OurDummy.next = head
    OurPrefixSumToNode = {}
    OurPrefixSum = 0
    OurCurrentNode = OurDummy
    while OurCurrentNode:
        OurPrefixSum += OurCurrentNode.val
        if OurPrefixSum in OurPrefixSumToNode:
            OurPreviousNode = OurPrefixSumToNode[OurPrefixSum]
            OurToRemuve = OurPreviousNode.next
            OurSum = OurPrefixSum + (OurToRemuve.val if OurToRemuve else 0)
            while OurSum != OurPrefixSum:
                del OurPrefixSumToNode[OurSum]
                OurToRemuve = OurToRemuve.next
                OurSum += OurToRemuve.val if OurToRemuve else 0
            OurPreviousNode.next = OurCurrentNode.next
        else:
            OurPrefixSumToNode[OurPrefixSum] = OurCurrentNode
        OurCurrentNode = OurCurrentNode.next
    return OurDummy.next

OurHead = ListNode()
OurHead = [1,2,3,-3,-2]
print(removeZeroSumSublists1(OurHead))
