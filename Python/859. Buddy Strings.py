# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
#
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

from collections import defaultdict


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if (n != len(goal)) or (set(s) != set(goal)):
            return False

        our_count, our_equals = 0, False
        our_dict_s = defaultdict(int)
        our_dict_g = defaultdict(int)
        for i in range(n):
            if s[i] != goal[i]:
                our_count += 1

            our_dict_s[s[i]] += 1
            our_dict_g[goal[i]] += 1
            if our_dict_s[s[i]] >= 2: our_equals = True

        return (our_count == 2 and our_dict_s == our_dict_g) or (our_count == 0 and our_equals and our_dict_s == our_dict_g)

s = "abcaa"
goal = "abcbb"
x = Solution()
print(x.buddyStrings(s, goal))