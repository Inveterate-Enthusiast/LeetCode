# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        our_dict = defaultdict(list)
        for s in strs:
            ss = tuple(sorted([i for i in s]))
            our_dict[ss].append(s)

        return list(our_dict.values())

strs = ["ddddddddddg","dgggggggggg"]
x = Solution()
print(x.groupAnagrams(strs))