# You are given a string s consisting of lowercase English letters, and an integer k.
#
# Your task is to delete some (possibly none) of the characters in the string so that
# the number of distinct characters in the resulting string is at most k.
#
# Return the minimum number of deletions required to achieve this.

from collections import defaultdict

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        our_dict = defaultdict(int)
        for i in s:
            our_dict[i] += 1
        n = len(our_dict)
        if n <= k:
            return 0

        our_tuple = sorted([(key, value) for key, value in our_dict.items()], key=lambda x: x[1])
        result = 0
        i = 0
        while (n - i) > k:
            result += our_tuple[i][1]
            i += 1
        return result

s = "yyyzz"
k = 1
x = Solution()
print(x.minDeletion(s, k))