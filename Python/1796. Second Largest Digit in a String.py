# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
#
# An alphanumeric string is a string consisting of lowercase English letters and digits.
from torchgen.api.functionalization import reverse_name


class Solution:
    def secondHighest(self, s: str) -> int:
        our_set = set()
        for i in s:
            if i.isnumeric():
                our_set.add(int(i))
        our_list = list(our_set)
        result = (-1) if not our_list or len(our_list) == 1 else sorted(our_list, reverse=True)[1]
        return result

s = "dfa12321afd"
x = Solution()
print(x.secondHighest(s))