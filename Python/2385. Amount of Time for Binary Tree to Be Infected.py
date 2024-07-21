# You are given the root of a binary tree with unique values, and an integer start.
# At minute 0, an infection starts from the node with value start.
#
# Each minute, a node becomes infected if:
#
# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def built(lst:List) -> Optional[TreeNode]:
    if not lst:
        return TreeNode()

    _root = TreeNode(val=lst[0])
    _queue = deque()
    _queue.append(_root)
    i = 1
    while i < len(lst):
        curNode = _queue.popleft()
        if i < len(lst) and lst[i] != "null":
            curNode.left = TreeNode(val=lst[i])
            _queue.append(curNode.left)
        i += 1
        if i < len(lst) and lst[i] != "null":
            curNode.right = TreeNode(val=lst[i])
            _queue.append(curNode.right)
        i += 1
    return _root

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

        _queue = deque()
        _startNode = None; totalSteps = -1
        root.parent = None; root.infected = False; _queue.append(root)
        while _queue:
            tempNode = _queue.popleft()
            if tempNode.val == start:
                _startNode = tempNode

            if tempNode.left:
                tempNode.left.parent = tempNode
                tempNode.left.infected = False
                _queue.append(tempNode.left)

            if tempNode.right:
                tempNode.right.parent = tempNode
                tempNode.right.infected = False
                _queue.append(tempNode.right)

        _startNode.infected = True
        _queue.append((_startNode, 0))
        while _queue:
            curLen = len(_queue)
            for _ in range(curLen):
                curNode, curStep = _queue.popleft()
                totalSteps = max(totalSteps, curStep)

                if curNode.left and not curNode.left.infected:
                    curNode.left.infected = True
                    _queue.append((curNode.left, curStep + 1))

                if curNode.right and not curNode.right.infected:
                    curNode.right.infected = True
                    _queue.append((curNode.right, curStep + 1))

                if curNode.parent and not curNode.parent.infected:
                    curNode.parent.infected = True
                    _queue.append((curNode.parent, curStep + 1))

        return totalSteps



root = [1,5,3,"null",4,10,6,9,2]; start = 3
OurRoot = built(root)
X = Solution()
print(X.amountOfTime1(OurRoot, start))
