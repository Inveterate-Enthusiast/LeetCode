# You need to construct a binary tree from a string consisting of parenthesis and integers.
#
# The whole input represents a binary tree. It contains an integer followed by zero,
# one or two pairs of parenthesis.
# The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
#
# You always start to construct the left child node of the parent first if it exists.
from typing import List, Optional, Tuple
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        OurStack = deque()
        lBr, rBr = "(", ")"
        root = None; tempDigit = None; minusFlag = False
        for char in s:
            if char == "-":
                minusFlag = True
            elif char.isdigit():
                tempDigit = int(char) if tempDigit is None else tempDigit * 10 + int(char)
            else:
                tempDigit = tempDigit if not minusFlag else (tempDigit * (-1))
                minusFlag = False
                if tempDigit is not None: tempNode = TreeNode(val=tempDigit)

                if OurStack and tempNode:
                    if OurStack[-1][1] == lBr:
                        OurStack[-1][0].left = tempNode
                        OurStack[-1][1] = rBr
                    elif OurStack[-1][1] == rBr:
                        OurStack[-1][0].right = tempNode

                if tempNode: OurStack.append([tempNode, lBr])
                if char == rBr:
                    OurStack.pop()

                if not root: root = tempNode
                tempDigit = None
                tempNode = None
        else:
            if tempDigit:
                tempDigit = tempDigit if not minusFlag else (tempDigit * (-1))
                minusFlag = False
                tempNode = TreeNode(val=tempDigit)
                if OurStack and tempNode:
                    if OurStack[-1][1] == lBr:
                        OurStack[-1][0].left = tempNode
                        OurStack[-1][1] = rBr
                    elif OurStack[-1][1] == rBr:
                        OurStack[-1][0].right = tempNode
                if not root: root = tempNode
        return root

s = "4"
X = Solution()
print(X.str2tree(s))