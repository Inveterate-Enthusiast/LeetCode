# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
#
# If the town judge exists, then:
#
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
# If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
#
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n == 1:
                return 1
            else:
                return -1

        our_dict = defaultdict(int)
        our_set = set()
        for i in trust:
            our_set.add(i[0])
            our_dict[i[1]] += 1

        for k, v in our_dict.items():
            if not k in our_set and v == (n-1):
                return k
        return -1

n = 2
trust = [[1,2]]
x = Solution()
print(x.findJudge(n, trust))