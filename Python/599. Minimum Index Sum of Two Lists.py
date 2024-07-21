# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
#
# A common string is a string that appeared in both list1 and list2.
#
# A common string with the least index sum is a common string such that
# if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
#
# Return all the common strings with the least index sum. Return the answer in any order.
from typing import List, Optional

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        _dict = {i: 0 for i in set(list1).intersection(set(list2))}

        for index, string in enumerate(list1):
            if string in _dict:
                _dict[string] = index

        OurMin = float("inf"); ansList = list()
        for index, string in enumerate(list2):
            if string in _dict:
                _dict[string] = (x := _dict[string] + index)
                if x < OurMin:
                    OurMin = x
                    ansList = list([string])
                elif x == OurMin:
                    ansList.append(string)

        return ansList





list1 = ["Shogun","Tapioca Express","Burger King","KFC"]; list2 = ["KFC","Shogun","Burger King"]
X = Solution()
print(X.findRestaurant(list1, list2))

