# You are given the head of a doubly linked list, which contains nodes that have a next pointer and a previous pointer.
#
# Return an integer array which contains the elements of the linked list in order.

from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        our_list = list()
        our_list.append(root)
        temp_node = root.next
        while temp_node:
            our_list.append(temp_node.val)
            temp_node = temp_node.next

        return our_list