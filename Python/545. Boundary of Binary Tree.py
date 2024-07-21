# The boundary of a binary tree is the concatenation of the root, the left boundary,
# the leaves ordered from left-to-right, and the reverse order of the right boundary.
#
# The left boundary is the set of nodes defined by the following:
#
# The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
# If a node in the left boundary and has a left child, then the left child is in the left boundary.
# If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
# The leftmost leaf is not in the left boundary.
# The right boundary is similar to the left boundary, except it is the right side of the root's right subtree.
# Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.
#
# The leaves are nodes that do not have any children. For this problem, the root is not a leaf.
#
# Given the root of a binary tree, return the values of its boundary.
from typing import List, Optional, Tuple
from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build(lst:list) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()
    OurQueue = deque()
    root = TreeNode(val=lst[0])
    OurQueue.append(root)
    i = 1
    while i < len(lst):
        curNode = OurQueue.popleft()
        if i < len(lst) and lst[i] != "null":
            curNode.left = TreeNode(val=lst[i])
            OurQueue.append(curNode.left)
        i += 1

        if i < len(lst) and lst[i] != "null":
            curNode.right = TreeNode(val=lst[i])
            OurQueue.append(curNode.right)
        i += 1
    return root

class CustomValue:
    def __init__(self, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.left = left
        self.right = right

def CustomValue_factory():
    return CustomValue()


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        OurDict = defaultdict(CustomValue_factory)
        OurQueue1 = deque(); OurQueue1.append(root)
        OurQueue2 = deque()
        curLevel = 0

        while OurQueue1:
            curLevel += 1
            curLen = len(OurQueue1)
            OurQueue2 = deque()
            for i in range(curLen):
                tempNode = OurQueue1[i]

                if tempNode.left: OurQueue2.append(tempNode.left)
                if tempNode.right: OurQueue2.append(tempNode.right)

            if OurQueue2:
               OurDict[curLevel].left = OurQueue1[0]
               OurDict[curLevel].right = OurQueue1[-1]
               OurQueue1 = OurQueue2
            else:
                OurQueue2 = OurQueue1
                OurQueue1 = deque()

        ansList = list()
        for i in range(1, curLevel):
            ansList.append(OurDict[i].left.val)

        ansList.extend([j.val for j in OurQueue2])

        for i in range(curLevel - 1, -1, -1):
            if not OurDict[i].left is OurDict[i].right:
                ansList.append(OurDict[i].right.val)

        return ansList

    def boundaryOfBinaryTree1(self, root: Optional[TreeNode]) -> List[int]:
        self.ansList = list()
        self.leftSide = "left"
        self.rightSide = "right"

        def dfs(node: Optional[TreeNode], side: Optional[str]):
            if not node:
                return None

            if not side or side == self.leftSide:
                self.ansList.append(node.val)
            left = dfs(node.left, self.leftSide)
            right = dfs(node.right, self.rightSide)


        return self.ansList


null = "null"
root = [1,null,2,3,4]
OurRoot = build(root)
X = Solution()
print(X.boundaryOfBinaryTree(OurRoot))