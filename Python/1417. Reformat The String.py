# You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
#
# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit.
# That is, no two adjacent characters have the same type.
#
# Return the reformatted string or return an empty string if it is impossible to reformat the string.

from collections import deque

class Solution:
    def reformat(self, s: str) -> str:
        l, d = deque(), deque()
        for char in s:
            if char.isdigit():
                d.append(char)
            elif char.isalpha():
                l.append(char)
            else:
                return str()

        result = str()
        l, d = l if len(l) >= len(d) else d, d if len(l) >= len(d) else l
        while l and d:
            result += l.popleft()
            result += d.popleft()

        if len(l) == 1:
            result += l.popleft()
        elif len(d) == 1:
            result += d.popleft()

        return str() if len(l) > 1 or len(d) > 1 else result

s = "ab123"
x = Solution()
print(x.reformat(s))