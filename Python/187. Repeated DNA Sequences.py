# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
#
# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
#
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings)
# that occur more than once in a DNA molecule. You may return the answer in any order.

from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        our_dict = defaultdict(int)
        added = 10
        for i in range(n):
            if (i + added - 1) >= n:
                break
            our_dict[s[i:(i + added)]] += 1

        result = list()
        for seq, freq in our_dict.items():
            if freq > 1:
                result.append(seq)

        return result

    def findRepeatedDnaSequences1(self, s: str) -> List[str]:
        n = len(s)
        set_passes, set_added = set(), set()
        added = 10
        for i in range(n):
            if (i + added - 1) >= n:
                break
            seq = s[i:(i + added)]
            if seq in set_passes:
                set_added.add(seq)
            set_passes.add(seq)
        return list(set_added)

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
x = Solution()
print(x.findRepeatedDnaSequences1(s))