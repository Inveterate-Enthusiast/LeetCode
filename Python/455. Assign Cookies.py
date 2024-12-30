# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(); s.sort()
        i = j = 0
        result = 0
        while (i < len(g) and j < len(s)):
            if g[i] <= s[j]:
                result += 1
                i += 1; j += 1
            else:
                j += 1
        return result

g = [1, 2]; s = [1, 2, 3]
x = Solution()
print(x.findContentChildren(g, s))