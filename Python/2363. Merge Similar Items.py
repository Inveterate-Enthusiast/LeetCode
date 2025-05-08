# You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:
#
# items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
# The value of each item in items is unique.
# Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.
#
# Note: ret should be returned in ascending order by value.

from typing import List
from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        our_dict = defaultdict(int)
        for value, weight in (items1 + items2):
            our_dict[value] += weight

        result = sorted(our_dict.items(), key = lambda x: x[0])
        return result

items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
x = Solution()
print(x.mergeSimilarItems(items1, items2))