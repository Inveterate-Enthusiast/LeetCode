# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

from typing import Optional
import time
import random

start_time = time.time()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TwoWayNode:
    def __init__(self, valP=None, valQ=None, right=None, left=None):
        self.valP = valP
        self.valQ = valQ
        self.right = right
        self.left = left

def isSameTree1(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # решение через стек из двусвязного списка
    OurStackHead = TwoWayNode()
    tempPTreeNode = p
    tempQTreeNode = q
    while (OurStackHead.valP and OurStackHead.valQ) or (tempPTreeNode and tempQTreeNode):
        while tempPTreeNode and tempQTreeNode:
            if OurStackHead.valP is None and OurStackHead.valQ is None:
                OurStackHead.valP = tempPTreeNode
                OurStackHead.valQ = tempQTreeNode
            elif OurStackHead.right is None:
                OurStackHead.right = OurStackHead.left = TwoWayNode(valP=tempPTreeNode, valQ=tempQTreeNode, right=OurStackHead, left=OurStackHead)
            else:
                OurStackHead.left.right = TwoWayNode(valP=tempPTreeNode, valQ=tempQTreeNode, right=OurStackHead, left=OurStackHead.left)
                OurStackHead.left = OurStackHead.left.right
            tempPTreeNode = tempPTreeNode.left
            tempQTreeNode = tempQTreeNode.left
        else:
            if (tempPTreeNode.val if tempPTreeNode else None) != (tempQTreeNode.val if tempQTreeNode else None):
                return False

        if OurStackHead.right:
            tempPTreeNode = OurStackHead.left.valP
            tempQTreeNode = OurStackHead.left.valQ
            if OurStackHead.left.left is not OurStackHead:
                OurStackHead.left = OurStackHead.left.left
                OurStackHead.left.right = None
            else:
                OurStackHead.left = None
                OurStackHead.right = None

        else:
            tempPTreeNode = OurStackHead.valP
            tempQTreeNode = OurStackHead.valQ
            OurStackHead = TwoWayNode()

        if (tempPTreeNode.val if tempPTreeNode else None) != (tempQTreeNode.val if tempQTreeNode else None):
            return False
        else:
            tempPTreeNode = tempPTreeNode.right
            tempQTreeNode = tempQTreeNode.right
    else:
        if (tempPTreeNode.val if tempPTreeNode else None) != (tempQTreeNode.val if tempQTreeNode else None):
            return False
    return True

def isSameTree2(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # через стек в виде массива
    OurStack = []
    tempTreeNodeP = p
    tempTreeNodeQ = q
    while OurStack or (tempTreeNodeP and tempTreeNodeQ):
        while (tempTreeNodeP and tempTreeNodeQ):
            OurStack.append((tempTreeNodeP, tempTreeNodeQ))
            tempTreeNodeP = tempTreeNodeP.left
            tempTreeNodeQ = tempTreeNodeQ.left
        else:
            if (tempTreeNodeP.val if tempTreeNodeP else None) != (tempTreeNodeQ.val if tempTreeNodeQ else None):
                return False

        tempTreeNodeP = OurStack[-1][0]
        tempTreeNodeQ = OurStack[-1][1]
        OurStack.pop()
        if tempTreeNodeP.val != tempTreeNodeQ.val:
            return False

        tempTreeNodeP = tempTreeNodeP.right
        tempTreeNodeQ = tempTreeNodeQ.right

    else:
        if (tempTreeNodeP.val if tempTreeNodeP else None) != (tempTreeNodeQ.val if tempTreeNodeQ else None):
            return False
    return True

def isSameTree3(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # решение через рекурсию
    if not p and not q: # 1-ый крайний случай
        return True
    elif not p or not q: # 2-ой крайний случай
        return False
    elif p.val != q.val: # 3-ий крайний случай
        return False
    return isSameTree3(p.left, q.left) and isSameTree3(p.right, q.right)


def build_simple_binary_tree(root:list):
    if not root:
        return None

    queue = []
    root_node = TreeNode(val=root[0])
    queue.append(root_node)
    i = 1

    while i < len(root):
        curNode = queue.pop(0)
        if i < len(root) and root[i] != "null":
            curNode.left = TreeNode(val=root[i])
            queue.append(curNode.left)
        i += 1

        if i < len(root) and root[i] != "null":
            curNode.right = TreeNode(val=root[i])
            queue.append(curNode.right)
        i += 1

    return root_node


p = [random.randint(0,700) for _ in range(9000)]
q = p.copy()

OurPTree = build_simple_binary_tree(p)
OurQTree = build_simple_binary_tree(q)


print(isSameTree3(OurPTree, OurQTree))
end_time = time.time()
print(f"Время выполнения составило: {end_time-start_time}")