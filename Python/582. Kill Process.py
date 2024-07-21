# You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid,
# where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.
#
# Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0,
# which means this process has no parent process (the root of the tree).
#
# When a process is killed, all of its children processes will also be killed.
#
# Given an integer kill representing the ID of a process you want to kill, return a list
# of the IDs of the processes that will be killed. You may return the answer in any order.

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
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        self.OurDict = defaultdict(list)
        self.ansSet = set()

        for child, parent in enumerate(ppid):
            if not parent == 0: self.OurDict[parent].append(pid[child])

        def add_to_kill(kill: int):
            self.ansSet.add(kill)
            for to_kill in self.OurDict[kill]:
                add_to_kill(to_kill)

        add_to_kill(kill)

        return list(self.ansSet)




pid = [1,2,3,4,5]; ppid = [0,1,1,1,1]; kill = 1
X = Solution()
print(X.killProcess(pid, ppid, kill))