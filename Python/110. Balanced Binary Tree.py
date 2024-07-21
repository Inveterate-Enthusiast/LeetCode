# Given a binary tree, determine if it is height-balanced.


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TwoWaysLinkedList:
    head = None

    class Node:
        def __init__(self, element=None, status=None, next_node=None, prev_node=None):
            self.element = element
            self.status = status
            self.next_node = next_node
            self.prev_node = prev_node

    def append(self, element, status):
        if not self.head:
            self.head = self.Node(element=element, status=status)
        elif not self.head.next_node:
            self.head.next_node = self.head.prev_node = self.Node(element=element, status=status, next_node=self.head, prev_node=self.head)
        else:
            self.head.prev_node.next_node = self.Node(element=element, status=status, next_node=self.head, prev_node=self.head.prev_node)
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
        return (Node.element, Node.status)

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

def check_max_height(node:Optional[TreeNode]) -> int:
    if not node:
        return 0
    return 1 + max(check_max_height(node.left), check_max_height(node.right))

def isBalanced1(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    return abs(check_max_height(root.left)-check_max_height(root.right)) <= 1 and isBalanced1(root.left) and isBalanced1(root.right)


def isBalanced2(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    OurHeightDict = {}
    OurStack = [(root, False)] # second argument means its status

    while OurStack:
        curNode, VisStatus = OurStack.pop()
        if curNode:
            if not VisStatus:
                OurStack.append((curNode, True))
                OurStack.append((curNode.left, False)); OurStack.append((curNode.right, False))
            else:
                leftHeight = OurHeightDict.get(curNode.left, 0)
                rightHeight = OurHeightDict.get(curNode.right, 0)
                if abs(rightHeight - leftHeight) >= 2:
                    return False
                else:
                    OurHeightDict[curNode] = 1 + max(leftHeight, rightHeight)

    return True

def isBalanced3(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    OurStack = TwoWaysLinkedList()
    OurStack.append(element=root, status=False)
    OurHeightDict = dict()

    while OurStack.head:
        curNode, VisStatus = OurStack.pop()
        if curNode:
            if not VisStatus:
                OurStack.append(element=curNode, status=True)
                OurStack.append(element=curNode.left, status=False)
                OurStack.append(element=curNode.right, status=False)
            else:
                leftHeight = OurHeightDict.get(curNode.left, 0)
                rightHeight = OurHeightDict.get(curNode.right, 0)
                if abs(rightHeight-leftHeight) >= 2:
                    return False
                else:
                    OurHeightDict[curNode] = 1 + max(leftHeight, rightHeight)
    return True

root = [3,9,20,"null","null",15,7]
OurRoot = build_simple_binary_tree(root)
print(isBalanced3(OurRoot))