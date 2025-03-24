# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_set, s2_set = set(), set()
        s1_set_dubble, s2_set_dubble = set(), set()
        for i in s1.split():
            if not i in s1_set and not i in s1_set_dubble:
                s1_set.add(i)
            else:
                s1_set.discard(i)
                s1_set_dubble.add(i)

        for i in s2.split():
            if not i in s2_set and not i in s2_set_dubble:
                s2_set.add(i)
            else:
                s2_set.discard(i)
                s2_set_dubble.add(i)
        return list((s1_set ^ s2_set) - (s1_set_dubble ^ s2_set_dubble))

s1 = "this apple is sweet apple apple"
s2 = "this apple is sour"
x = Solution()
print(x.uncommonFromSentences(s1, s2))