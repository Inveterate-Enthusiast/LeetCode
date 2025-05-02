# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
#
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
#
# Return names sorted in descending order by the people's heights.

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        our_dict = dict()
        n = len(names)
        for i in range(n):
            our_dict[heights[i]] = names[i]

        heights_sorted = sorted(heights, reverse=True)
        result = list()
        for i in range(n):
            result.append(our_dict[heights_sorted[i]])
        return result

names = ["Mary","John","Emma"]
heights = [180,165,170]
x = Solution()
print(x.sortPeople(names, heights))