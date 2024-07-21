# Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

from typing import List, Optional
from collections import deque

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        _stack = deque()
        minVal = float("-inf")
        for curVal in preorder:
            while _stack and _stack[-1] < curVal:
                minVal = _stack.pop()
            if curVal < minVal:
                return False
            _stack.append(curVal)
        return True

preorder = [5,2,1,3,6]
X = Solution()
print(X.verifyPreorder(preorder))