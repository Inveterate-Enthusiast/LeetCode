# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        _set = set()
        _dict = defaultdict()
        for index, char in enumerate(s):
            if not char in _set:
                if char in _dict:
                    del _dict[char]
                    _set.add(char)
                else:
                    _dict[char] = index

        return (-1) if not _dict else next(iter(_dict.values()))




s = "loveleetcode"
X = Solution()
print(X.firstUniqChar(s))
