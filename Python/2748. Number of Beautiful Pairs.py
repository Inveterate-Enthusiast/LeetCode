# You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length is called beautiful
# if the first digit of nums[i] and the last digit of nums[j] are coprime.
#
# Return the total number of beautiful pairs in nums.
#
# Two integers x and y are coprime if there is no integer greater than 1 that divides both of them.
# In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.

from typing import List
from itertools import combinations
from collections import defaultdict

class Solution:
    def gcd(self, x, y):
        x, y = max(x, y), min(x, y)
        while (x % y) != 0:
            x, y = y, (x % y)
        return y

    def countBeautifulPairs(self, nums: List[int]) -> int:
        our_combs = combinations(nums, 2)
        result = 0
        for x, y in our_combs:
            if self.gcd(int(str(x)[0]), int(str(y)[-1])) == 1:
                result += 1
        return result

    def countBeautifulPairs1(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        result = 0
        for num in nums:
            x = int(str(num)[-1])
            y = int(str(num)[0])
            for key, value in our_dict.items():
                if self.gcd(x, key) == 1:
                    result += value
            our_dict[y] += 1
        return result

nums = [31,25,72,79,74]
x = Solution()
print(x.countBeautifulPairs1(nums))