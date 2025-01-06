# You are keeping the scores for a baseball game with strange rules.
# At the beginning of the game, you start with an empty record.
#
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
#
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
#
# The test cases are generated such that the answer and all intermediate calculations
# fit in a 32-bit integer and that all operations are valid.
from typing import List
from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        queue = deque()
        for op in operations:
            try:
                queue.append(int(op))
            except Exception as e:
                if op == "+":
                    if queue and (not queue[-1] is queue[-2]):
                        queue.append(queue[-1] + queue[-2])
                elif op == "D":
                    if queue:
                        queue.append(queue[-1] * 2)
                elif op == "C":
                    queue.pop()
        return sum(queue)

ops = ["5","2","C","D","+"]
x = Solution()
print(x.calPoints(ops))