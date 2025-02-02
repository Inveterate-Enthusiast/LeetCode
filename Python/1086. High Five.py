# Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from
# a student with IDi, calculate each student's top five average.
#
# Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj
# and their top five average. Sort result by IDj in increasing order.
#
# A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

from typing import List
import heapq
import numpy as np
from collections import defaultdict

class MinHeap:
    def __init__(self):
        self._max_size = 5
        self.queue = list()

    def push_score(self, score):
        if len(self.queue) < 5:
            heapq.heappush(self.queue, score)
        else:
            heapq.heappushpop(self.queue, score)

    def calc_avg(self):
        return int((sum(self.queue) / self._max_size))

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        our_dict = defaultdict(MinHeap)
        for i in items:
            our_dict[i[0]].push_score(i[1])

        result = list()
        for k, v in our_dict.items():
            result.append([k, v.calc_avg()])

        return sorted(result, key=lambda x: x[0])

items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
x = Solution()
print(x.highFive(items))