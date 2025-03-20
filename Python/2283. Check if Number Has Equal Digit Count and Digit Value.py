# You are given a 0-indexed string num of length n consisting of digits.
#
# Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

from collections import defaultdict

class Solution:
    def digitCount(self, num: str) -> bool:
        our_dict = defaultdict(int)
        for i in num:
            our_dict[int(i)] += 1

        for i in range(len(num)):
            if our_dict[i] != int(num[i]):
                return False

        return True

num = "1210"
x = Solution()
print(x.digitCount(num))