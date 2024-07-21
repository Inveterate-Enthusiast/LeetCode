# You are given the root of a binary tree and an integer k. Besides the left and right children,
# every node of this tree has two other properties, a string node.val containing only lowercase English letters (possibly empty)
# and a non-negative integer node.len. There are two types of nodes in this tree:
#
# Leaf: These nodes have no children, node.len = 0, and node.val is some non-empty string.
# Internal: These nodes have at least one child (also at most two children), node.len > 0, and node.val is an empty string.
# The tree described above is called a Rope binary tree. Now we define S[node] recursively as follows:
#
# If node is some leaf node, S[node] = node.val,
# Otherwise if node is some internal node, S[node] = concat(S[node.left], S[node.right]) and S[node].length = node.len.
# Return k-th character of the string S[root].
#
# Note: If s and p are two strings, concat(s, p) is a string obtained by concatenating p to s. For example, concat("ab", "zz") = "abzz".
from typing import Optional, List
from collections import deque

class RopeTreeNode(object):
    def __init__(self, len=0, val="", left=None, right=None):
        self.len = len
        self.val = val
        self.left = left
        self.right = right

def built_simple_Rope_binary_tree(lst:list) -> Optional[RopeTreeNode]:
    if not lst:
        return RopeTreeNode()

    OurQueue = deque()
    OurRoot = RopeTreeNode()
    if isinstance(lst[0], str):
        OurRoot.val = lst[0]
    elif isinstance(lst[0], int):
        OurRoot.len = lst[0]
    else:
        return False
    OurQueue.append(OurRoot)
    i = 1
    while i < len(lst):
        tempNode = OurQueue.popleft()
        if i < len(lst) and lst[i] != "null":
            if isinstance(lst[i], str):
                tempNode.left = RopeTreeNode(val=lst[i])
            elif isinstance(lst[i], int):
                tempNode.left = RopeTreeNode(len=lst[i])
            else:
                return False
            OurQueue.append(tempNode.left)
        i += 1

        if i < len(lst) and lst[i] != "null":
            if isinstance(lst[i], str):
                tempNode.right = RopeTreeNode(val=lst[i])
            elif isinstance(lst[i], int):
                tempNode.right = RopeTreeNode(len=lst[i])
            else:
                return False
            OurQueue.append(tempNode.right)
        i += 1
    return OurRoot

class Solution:
    def getKthCharacter1(self, root: Optional[RopeTreeNode], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        OurStack = deque()
        OurStack.append((root, False))
        OurDict = dict()
        while OurStack:
            tempNode, OurFlag = OurStack.pop()
            if not OurFlag:
                OurStack.append((tempNode, True))
                if tempNode.left: OurStack.append((tempNode.left, False))
                if tempNode.right: OurStack.append((tempNode.right, False))
            else:
                if tempNode.len == 0:
                    OurDict[tempNode] = tempNode.val
                else:
                    leftStr = OurDict.get(tempNode.left, "")
                    rightStr = OurDict.get(tempNode.right, "")
                    OurDict[tempNode] = leftStr + rightStr
        return OurDict[root][k-1] if k <= len(OurDict[root]) else ""


root = ["ropetree"]; k = 8
OurRoot = built_simple_Rope_binary_tree(root)
X = Solution()
print(X.getKthCharacter1(OurRoot, k))








