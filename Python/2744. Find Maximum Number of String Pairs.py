# You are given a 0-indexed array words consisting of distinct strings.
#
# The string words[i] can be paired with the string words[j] if:
#
# The string words[i] is equal to the reversed string of words[j].
# 0 <= i < j < words.length.
# Return the maximum number of pairs that can be formed from the array words.
#
# Note that each string can belong in at most one pair.

from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        our_set = set()
        result = 0
        for i in words:
            if i[::-1] in our_set:
                result += 1
            our_set.add(i)

        return result

words = ["cd","ac","dc","ca","zz"]
x = Solution()
print(x.maximumNumberOfStringPairs(words))