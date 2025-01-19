# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length
# and answer[i] is the distance from index i to the closest occurrence of character c in s.
#
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = [0] * len(s)
        idx_list = list()
        for index, char in enumerate(s):
            if char == c:
                idx_list.append(index)

        our_len = len(idx_list)
        left, right = 0, 1
        for i in range(len(result)):
            if abs(i - idx_list[left]) > (abs(i - idx_list[right]) if right < our_len else float("inf")):
                left, right = right, right+1
            result[i] = abs(i - idx_list[left])
        return result

s = "loveleetcode"
c = "e"
x = Solution()
print(x.shortestToChar(s, c))