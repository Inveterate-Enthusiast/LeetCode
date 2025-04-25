# You are given an integer n that consists of exactly 3 digits.
#
# We call the number n fascinating if, after the following modification, the resulting number contains
# all the digits from 1 to 9 exactly once and does not contain any 0's:
#
# Concatenate n with the numbers 2 * n and 3 * n.
# Return true if n is fascinating, or false otherwise.
#
# Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.

from collections import defaultdict

class Solution:
    def isFascinating(self, n: int) -> bool:
        nn = list(map(int, str(n) + str(n * 2) + str(n * 3)))
        our_set = {i for i in range(1, 9 + 1)}
        our_dict = defaultdict(int)
        if len(set(nn) ^ our_set) > 0:
            return False

        for i in nn:
            our_dict[i] += 1
            if our_dict[i] > 1: return False

        return True


n = 192
x = Solution()
print(x.isFascinating(n))