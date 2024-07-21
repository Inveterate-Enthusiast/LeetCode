# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

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

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return list()

        _queue = deque()
        _queue.append(root)
        ansList = list()
        while _queue:
            curLen = len(_queue)
            curMax = float("-inf")
            for _ in range(curLen):
                tempNode = _queue.popleft()
                curMax = max(curMax, tempNode.val)

                if tempNode.left: _queue.append(tempNode.left)
                if tempNode.right: _queue.append(tempNode.right)
            else:
                ansList.append(curMax)

        return ansList

    def largestValues1(self, root: Optional[TreeNode]) -> List[int]:
        self._dict = defaultdict(int)
        self._list = list()

        def dfs(node:Optional[TreeNode], level:Optional[int]):
            if not node:
                return None

            self._dict[level] = max(self._dict[level], node.val) if level in self._dict else node.val
            left = dfs(node.left, level+1)
            right = dfs(node.right, level+1)

        dfs(root, 0)
        i = 0
        while i in self._dict:
            self._list.append(self._dict[i])
            i += 1
        return self._list

null = "null"
root = [-40,0,-37,17,-87,-13,62,82,-57,45,-52,3,-22,-55,-54,11,-2,60,69,-21,23,36,-100,6,-80,93,-55,67,78,-22,-70,-44,null,17,-38,77,-13,97,-22,66,-42,89,-69,-51,-2,-16,-72,-29,-49,-13,76,null,null,-56,-79,-4,84,-79,-71,-58,null,-59,71,-20,38,null,null,27,-47,46,42,-19,66,84,-4,null,null,null,null,null,null,78,-28,-3,12,21,-27,null,39,-15,-99,51,-14,38,78,56,-24,58,59,42,24,-26,18,-63,null,-3,77,null,null,-52,null,74,-55,null,-91,-80,-86,-23,null,11,-60,-84,null,null,null,null,null,-59,-45,-13,null,90,-3,-38,-5,1,-1,-90,null,53,-57,-25,32,-94,-52,-31,-90,65,85,23,62,null,null,70,-15,22,-37,7,26,81,94,23,48,-82,96,-91,-12,67,5,61,59,25,-45,-25,88,-20,64,-18,-55,42,-59,21,-69,-2,-36,34,17,null,null,-20,14,41,19,null,null,84,-55,-68,-88,98,-29,-46,10,97,-92,10,null,null,98,-31,76,null,null,-29,null,-12,-52,-21,-14,59,75,31,null,89,null,70,null,4,null,61,53,62,23,25,27,-62,-52,null,-99,null,null,88,88,63,null,null,null,null,null,-43,null,-92,23,-49,53,68,-44,-73,-95,81,21,-77,39,-41,-62,3,25,null,null,null,null,null,-44,null,null,63,null,-54,-13,null,null,-83,52,-57,29,78,62,83,null,54,null,74,53,null,8,33,66,32,21,null,51,-94,25,5,16,null,-81,null,null,null,null,null,null,-28,17,76,18,85,null,-65,null,null,null,null,null,75,null,-26,49,69,-9,-51,null,-11,null,null,3,-38,0,-61,-43,60,null,null,79,null,-84,null,null,-81,-38,-43,20,-97,-72,null,null,null,53,38,null,69,null,-67,38,null,null,null,null,null,-67,-91,-96,81,44,null,null,-97,null,null,null,33,51,60,null,null,null,null,49,null,null,-6,null,-63,null,null,71,null,null,null,-34,null,null,-58,98,50,-85,6,23,-34,93,-52,83,20,-9,33,null,-26,-85,-36,-56,26,-13,-35,-73,-17,-97,-42,86,42,null,95,67,null,63,null,null,null,null,25,null,null,null,null,-90,-59,8,86,null,null,null,-89,19,31,68,-32,null,null,-84,null,null,-59,null,null,86,-56,null,null,-20,-26,-11,37,null,12,null,null,null,-9,80,null,-27,null,58,-37,null,73,null,null,null,-70,-75,-17,null,null,null,null,null,-46,null,null,15,null,-75,74,43,54,43,-35,null,-14,null,-22,null,null,null,null,-96,66,null,-8,-8,null,null,null,null,-74,null,-43,-33,25,null,-43,-49,98,97,-36,46,null,-81,-62,-2,null,null,null,null,null,-53,-6,-59,null,null,null,null,-16,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,-49,12,22,98,null,null,null,45,33,0,null,null,-95,91,-80,-88,-17,null,83,38,null,-99,-21,null,null,-81,-61,87,41,-35,37,19,-37,-12,7,null,-52,-93,62,-31,-18,-57,-29,-67,-73,57,3,-33,null,-79,-74,94,2,null,-85,-87,95,null,null,null,null,63,null,null,null,null,null,18,null,-74,null,-3,-96,null,46,27,-26,82,24,-96,null,null,null,null,46,null,null,null,null,37,null,null,null,4,-5,9,11,-86,null,-13,null,null,null,-68,null,null,6,null,null,null,null,null,null,null,null,null,null,null,71,24,3,null,-74,null,null,null,null,-66,-61,82,-47,null,null,null,93,null,null,null,null,61,null,-71,null,null,null,null,null,null,null,null,null,null,null,-93,64,-67,null,97,45,null,null,null,null,null,32,-61,null,-53,null,-14,-9,-91,null,93,-71,null,null,42,null,null,null,null,57,null,null,null,null,null,-2,null,null,-1,43,null,null,null,-30,null,null,50,36,89,-72,null,86,-7,-87,-94,72,null,2,71,7,null,null,null,45,-6,-2,-79,8,32,36,-98,-40,77,0,null,-19,null,29,78,null,null,-58,null,47,86,null,null,90,null,null,-14,null,-1,null,-65,49,null,null,72,70,null,null,null,null,null,90,null,null,-51,50,-73,-46,-34,5,7,null,null,35,null,null,null,null,null,null,32,null,null,null,null,-41,99,null,-98,-90,null,45,null,null,null,null,null,99,null,-6,null,null,null,-20,null,null,38,2,21,78,null,null,null,null,-30,null,null,-36,null,-5,68,null,40,-33,-92,null,null,17,null,null,83,null,null,null,null,33,null,null,null,null,-20,-95,null,null,-68,null,-9,-9,7,21,-47,71,-97,null,null,null,30,null,null,-69,null,null,-42,null,-65,null,40,98,null,null,6,null,-27,95,-26,-100,null,null,75,null,6,-77,null,null,null,null,-14,null,null,70,null,null,80,null,null,null,null,null,null,null,-59,null,74,null,30,null,-71,29,null,-4,-8,-55,-79,-91,19,14,34,null,-62,null,5,22,-38,null,null,null,null,null,null,-57,null,null,null,null,51,8,14,-17,-7,-79,-65,-68,69,50,-100,91,-1,66,31,28,null,19,-50,62,23,4,17,-83,-84,2,-22,null,null,null,null,null,9,37,-79,null,23,null,null,null,null,null,-74,11,-2,null,null,null,null,null,null,null,null,-74,null,null,-78,null,30,null,-82,null,-51,null,null,null,null,null,59,-90,null,-8,null,null,null,null,null,88,null,3,null,null,null,null,57,null,null,null,null,null,null,null,-26,null,null,-62,null,null,null,null,75,null,null,null,83,52,null,-31,null,null,-78,null,-71,9,87,34,null,51,28,null,null,-54,14,null,null,-25,-11,80,null,null,-20,-40,null,null,null,null,-28,null,null,null,-94,-46,null,-3,null,37,-70,-22,null,null,-89,-28,1,83,41,18,-9,null,-46,61,null,89,-17,-29,null,-32,-78,-20,15,null,72,null,-38,7,null,null,null,-13,50,-81,null,26,70,-94,null,null,-76,-3,52,20,null,91,40,91,null,null,null,null,null,null,32,null,null,null,40,37,29,-53,-45,-98,-57,-53,null,null,null,7,93,-37,-64,-65,null,92,-47,58,13,null,null,null,null,null,67,-48,null,-33,-46,null,null,null,-65,null,null,null,null,null,-49,-85,-58,null,null,62,null,null,null,null,null,null,null,null,-33,null,null,null,-47,null,null,null,null,null,null,-37,null,null,-91,-100,null,null,null,null,null,-59,null,27,null,null,null,42,null,null,null,null,-59,null,null,null,-25,38,20,-60,null,null,null,-1,-16,null,null,null,null,null,null,-15,-10,75,27,86,-2,-43,38,null,null,-82,null,null,null,null,null,80,75,60,89,-11,null,null,null,15,-93,75,55,-89,null,null,null,null,51,-40,null,null,-22,null,null,null,null,-49,-24,68,null,null,85,78,null,null,-96,29,51,74,-93,null,null,36,-26,null,null,3,-65,null,65,null,70,null,null,null,-81,-74,87,null,null,null,-54,39,99,-72,null,null,8,-14,null,null,null,null,-96,90,null,null,51,-61,null,-67,null,null,null,-65,null,null,-41,21,null,null,null,null,51,null,null,null,null,null,null,null,null,null,null,-26,null,null,null,-95,-52,null,null,null,null,null,null,null,null,null,null,null,97,null,-73,null,76,-52,4,null,null,57,-85,43,64,null,null,null,null,null,null,null,62,41,-100,-64,null,75,null,-99,null,-43,null,null,-64,-23,-68,null,null,null,71,-12,-62,93,18,null,-3,-66,96,-99,30,null,32,-41,-25,null,null,41,null,null,null,null,null,null,-32,-56,-32,0,null,49,null,null,null,null,-85,-60,53,null,null,null,-90,99,6,62,null,null,-52,null,null,null,-51,-4,null,null,null,-94,-94,null,-48,null,null,null,null,99,null,null,null,-93,null,-63,14,null,null,-83,32,null,41,null,null,74,null,null,null,null,49,null,80,null,null,null,null,null,null,null,null,null,null,50,null,-53,null,-71,null,null,null,null,null,null,null,null,-71,-51,48,null,null,31,null,null,26,7,null,null,-60,null,null,null,22,null,null,90,null,null,83,null,null,-84,-100,-18,null,null,null,-81,null,-9,-60,null,-97,null,-56,46,-56,88,-26,null,null,-76,null,95,null,null,null,53,-34,null,7,65,null,null,null,-63,-44,16,null,null,-28,null,-40,89,5,-87,-95,99,11,-18,-13,59,null,null,null,null,13,19,null,-24,70,91,null,20,16,null,null,null,null,null,null,null,94,null,null,null,null,62,null,null,null,null,null,null,38,null,68,14,42,null,null,84,75,null,56,null,-58,null,89,-72,15,-59,-98,-66,null,33,-33,27,-13,null,null,null,null,77,null,null,null,null,-39,null,94,-29,null,null,null,null,null,null,53,null,-73,88,null,null,null,null,null,35,null,null,null,57,53,null,-47,null,77,9,null,-17,-16,null,41,-48,60,89,78,-75,null,null,10,-89,39,null,-41,null,null,null,-21,84,null,null,56,12,null,64,null,null,null,null,null,null,null,null,null,null,84,null,null,null,null,null,null,null,null,null,null,null,null,84,-75,null,null,null,-23,null,null,null,null,null,null,null,61,null,null,89,null,null,null,null,null,null,-40,null,null,null,null,-57,null,null,null,null,-95,null,null,null,-97,null,null,null,null,null,null,null,-77,0,null,null,null,null,null,null,null,null,-30,null,null,67,-56,52,null,-29,null,null,-20,81,null,-55,-27,74,79,32,null,null,-33,-17,96,null,null,null,null,null,null,null,86,-16,null,null,null,null,-68,null,null,null,null,null,null,34,null,null,null,10,null,null,null,null,null,null,null,null,null,null,null,-85,null,56,22,-5,-77,null,null,null,null,-82,null,null,null,null,null,null,null,null,null,81,null,null,null,51,null,null,-22,null,null,null,null,null,null,null,null,null,null,-82,null,72,null,null,null,-30,1,null,null,null,-37,null,null,null,null,-85,null,null,null,null,null,null,null,null,null,null,null,3]
OurRoot = build(root)
X = Solution()
print(X.largestValues1(OurRoot))