# Given a string s, find any substring  of length 2 which is also present in the reverse of s.
#
# Return true if such a substring exists, and false otherwise.
import itertools
class Solution:
    def isSubstringPresent1(self, s: str) -> bool:
        rev_s = {s[i:i - 2 if i > 1 else None:-1] for i in range(len(s) - 1, 0, -1)}
        for i in range(len(s)-1):
            if s[i:i+2] in rev_s: return True
        return False

    def isSubstringPresent2(self, s: str) -> bool:
        rev_s = {s[i:i-2 if i > 1 else None:-1] for i in range(len(s)-1, 0, -1)}
        s = {s[i:i+2] for i in range(len(s)-1)}
        return bool(s.intersection(rev_s))

    def isSubstringPresent3(self, s: str) -> bool:
        return bool({s[i:i-2 if i > 1 else None:-1] for i in range(len(s)-1, 0, -1)}.intersection({s[i:i+2] for i in range(len(s)-1)}))

    def isSubstringPresent4(self, s: str) -> bool:
        return bool(set(itertools.pairwise(s)).intersection(set(itertools.pairwise(s[::-1]))))

X = Solution()
print(X.isSubstringPresent4("ausoe"))

