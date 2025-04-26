# You are given a 0-indexed integer array nums of even length.
#
# As long as nums is not empty, you must repetitively:
#
# Find the minimum number in nums and remove it.
# Find the maximum number in nums and remove it.
# Calculate the average of the two removed numbers.
# The average of two numbers a and b is (a + b) / 2.
#
# For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
# Return the number of distinct averages calculated using the above process.
#
# Note that when there is a tie for a minimum or maximum number, any can be removed.

from typing import List
from collections import deque, defaultdict

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        for i in nums:
            our_dict[i] += 1
        our_list = deque(sorted({i for i in our_dict.keys()}))
        our_set = set()
        while len(our_list) > 0:
            min, max = our_list[0], our_list[-1]
            if our_dict[min] == 1:
                our_list.popleft()
            our_dict[min] -= 1
            if our_dict[max] == 1:
                our_list.pop()
            our_dict[max] -= 1

            our_set.add((min + max) / 2)

        return len(our_set)


nums = [4,1,4,0,3,5]
x = Solution()
print(x.distinctAverages(nums))