# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_simple_binary_tree(root:list) -> Optional[TreeNode]:
    if not root:
        return TreeNode()

    OurQueue = []
    OurRoot = TreeNode(val=root[0])
    OurQueue.append(OurRoot)
    i = 1
    while i < len(root):
        curNode = OurQueue.pop(0)

        if i < len(root) and root[i] != "null":
            curNode.left = TreeNode(val=root[i])
            OurQueue.append(curNode.left)
        i += 1

        if i < len(root) and root[i] != "null":
            curNode.right = TreeNode(val=root[i])
            OurQueue.append(curNode.right)
        i += 1
    return OurRoot

class TwoWaysLinkedList:
    head = None

    class Node:
        def __init__(self, element=None, sum=None, next_node=None, prev_node=None):
            self.element = element
            self.sum = sum
            self.next_node = next_node
            self.prev_node = prev_node

    def append(self, element, sum):
        if not self.head:
            self.head = self.Node(element=element, sum=sum)
        elif not self.head.next_node:
            self.head.next_node = self.head.prev_node = self.Node(element=element, sum=sum, next_node=self.head, prev_node=self.head)
        else:
            self.head.prev_node.next_node = self.Node(element=element, sum=sum, next_node=self.head, prev_node=self.head.prev_node)
            self.head.prev_node = self.head.prev_node.next_node

    def pop(self):
        if not self.head:
            return (None, None)
        elif not self.head.next_node:
            Node = self.head
            self.head = self.head.next_node
        else:
            Node = self.head.prev_node
            if self.head.prev_node.prev_node is self.head:
                self.head.next_node = self.head.prev_node = None
            else:
                self.head.prev_node = self.head.prev_node.prev_node
                self.head.prev_node.next_node = self.head
        return (Node.element, Node.sum)

def hasPathSum1(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    OurStack = [(root, root.val)]

    while OurStack:
        curNode, curSum = OurStack.pop()
        if curNode:
            if not curNode.left and not curNode.right:
                if curSum == targetSum: return True
            else:
                if curNode.left: OurStack.append((curNode.left, curSum + curNode.left.val))
                if curNode.right: OurStack.append((curNode.right, curSum + curNode.right.val))
    return False

def hasPathSum2(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    elif not root.left and not root.right:
        return (targetSum-root.val) == 0
    else:
        return hasPathSum2(root.left, targetSum-root.val) or hasPathSum2(root.right, targetSum-root.val)



root = [5,4,8,11,"null",13,4,7,2,"null","null","null",1]; targetSum = 22
OurRoot = build_simple_binary_tree(root)
print(hasPathSum2(OurRoot, targetSum))







