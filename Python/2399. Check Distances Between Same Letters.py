# You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice.
# You are also given a 0-indexed integer array distance of length 26.
#
# Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
#
# In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i].
# If the ith letter does not appear in s, then distance[i] can be ignored.
#
# Return true if s is a well-spaced string, otherwise return false.

from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        our_dict = dict()
        char = "a"
        char_num = ord(char)
        char_num_temp = char_num
        while char != "z":
            char = chr(char_num_temp)
            our_dict[char] = (char_num_temp - char_num)
            char_num_temp += 1

        s_dict = dict()
        for index, i in enumerate(s):
            if i in s_dict:
                if distance[our_dict[i]] != (index - s_dict[i] - 1):
                    return False
            else:
                s_dict[i] = index

        return True

s = "abaccb"
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x = Solution()
print(x.checkDistances(s, distance))