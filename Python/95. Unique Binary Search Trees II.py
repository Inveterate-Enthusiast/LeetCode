# Given an integer n, return all the structurally unique BST's (binary search trees),
# which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees1(self, n: int) -> List[Optional[TreeNode]]:
        OurDict = {}
        def generate(left: int, right: int) -> List[Optional[TreeNode]]:
            if left > right:
                return [None]
            if (left, right) in OurDict:
                return OurDict[(left, right)]

            OurList = []
            for value in range(left, right + 1):
                for leftTree in generate(left, value - 1):
                    for rightTree in generate(value+1, right):
                        OurRoot = TreeNode(value, leftTree, rightTree)
                        OurList.append(OurRoot)
            OurDict[(left, right)] = OurList
            return OurList
        return generate(1, n)

    def generateTrees2(self, n: int) -> List[Optional[TreeNode]]:
        OurDict = dict()

        def generate_trees(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            elif (start, end) in OurDict:
                return OurDict[(start, end)]

            OurList = []
            for value in range(start, end+1):
                OurLeftTrees = generate_trees(start, value-1)
                OurRightTrees = generate_trees(value+1, end)

                for leftTree in OurLeftTrees:
                    for rightTree in OurRightTrees:
                        OurRoot = TreeNode(val=value, left=leftTree, right=rightTree)
                        OurList.append(OurRoot)

            OurDict[(start, end)] = OurList
            return OurList

        return generate_trees(1, n)

    def generateTrees3(self, n: int) -> List[Optional[TreeNode]]:
        OurDict = dict()

        def generate_trees(start:int, end:int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            elif (start, end) in OurDict:
                return OurDict[(start, end)]

            OurList = []
            for i in range(start, end+1):
                leftSubTreesList = generate_trees(start, i-1)
                rightSubTreesList = generate_trees(i+1, end)

                for leftSubTree in leftSubTreesList:
                    for rightSubTree in rightSubTreesList:
                        curTree = TreeNode(val=i, left=leftSubTree, right=rightSubTree)
                        OurList.append(curTree)

            OurDict[(start, end)] = OurList
            return OurList

        return generate_trees(1, n)

    def generateTrees4(self, n: int) -> List[Optional[TreeNode]]:
        OurDict = dict()

        def generateTrees(start:int, end:int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            elif (start, end) in OurDict:
                return OurDict[(start, end)]

            OurList = []

            for i in range(start, end+1):
                listOfLeftTrees = generateTrees(start, i-1)
                listofRightTrees = generateTrees(i+1, end)

                for leftTree in listOfLeftTrees:
                    for rightTree in listofRightTrees:
                        curTree = TreeNode(val=i, left=leftTree, right=rightTree)
                        OurList.append(curTree)

            OurDict[(start, end)] = OurList

            return OurList

        return generateTrees(1, n)

    def generateTrees5(self, n: int) -> List[Optional[TreeNode]]:
        if not n:
            return []

        def clone(node, c):
            if not node:
                return None
            return TreeNode(val=node.val+c, left=clone(node.left, c), right=clone(node.right, c))

        OurDict = dict()
        OurDict[0] = [None]
        OurDict[1] = [TreeNode(val=1)]

        for length in range(2, n+1):
            for rootVal in range(1, length+1):
                left_length = rootVal - 1
                right_length = length - rootVal

                for leftTree in OurDict[left_length]:
                    for rightTree in OurDict[right_length]:
                        curRoot = TreeNode(val=rootVal, left=leftTree, right=clone(rightTree, rootVal))
                        if length not in OurDict:
                            OurDict[length] = [curRoot]
                        else:
                            OurDict[length].append(curRoot)
        return OurDict[n]

    def generateTrees6(self, n: int) -> List[Optional[TreeNode]]:
        OurDict = dict()

        def generate_trees(start:int, end:int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            elif (start, end) in OurDict:
                return OurDict[(start, end)]

            OurList = []
            for rootVal in range(start, end+1):
                leftTreesList = generate_trees(start, rootVal-1)
                rightTreesList = generate_trees(rootVal+1, end)

                for leftTree in leftTreesList:
                    for rightTree in rightTreesList:
                        curTree = TreeNode(val=rootVal, left=leftTree, right=rightTree)
                        OurList.append(curTree)

            OurDict[(start, end)] = OurList
            return OurList

        return generate_trees(1, n)

    def generateTrees7(self, n: int) -> List[Optional[TreeNode]]:
        if not n:
            return []

        def clone(node, c):
            if not node:
                return None
            return TreeNode(val=node.val+c, left=clone(node.left, c), right=clone(node.right, c))

        OurDict = dict()
        OurDict[0] = [None]
        OurDict[1] = [TreeNode(val=1)]

        if n < 2:
            return OurDict[n]

        for length in range(2, n+1):
            for rootVal in range(1, length+1):
                left_length = rootVal - 1
                right_length = length - rootVal

                for leftTree in OurDict[left_length]:
                    for rightTree in OurDict[right_length]:
                        curRoot = TreeNode(val=rootVal, left=leftTree, right=clone(rightTree, rootVal))
                        OurDict.setdefault(length, []).append(curRoot)
        return OurDict[n]

    def generateTrees8(self, n: int) -> List[Optional[TreeNode]]:
        if not n:
            return []

        OurDict = dict()
        OurDict[0] = [None]
        OurDict[1] = [TreeNode(val=1)]

        def clone_tree(node, c):
            if not node:
                return None
            return TreeNode(val=node.val+c, left=clone_tree(node.left, c), right=clone_tree(node.right, c))

        for length in range(2, n+1):
            for rootVal in range(1, length+1):
                left_length = rootVal-1
                right_length = length-rootVal

                for leftTree in OurDict[left_length]:
                    for rightTree in OurDict[right_length]:
                        curRoot = TreeNode(val=rootVal, left=leftTree, right=clone_tree(rightTree, rootVal))
                        OurDict.setdefault(length, []).append(curRoot)

        return OurDict[n]



n = 3
X = Solution()
print(X.generateTrees8(n))









