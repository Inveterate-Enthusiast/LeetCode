# You are given a 0-indexed integer array nums of even length and there is also an empty array arr.
# Alice and Bob decided to play a game where in every round Alice and Bob will do one move.
# The rules of the game are as follows:
#
# Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
# Now, first Bob will append the removed element in the array arr, and then Alice does the same.
# The game continues until nums becomes empty.
# Return the resulting array arr.

from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = list()
        for i in range(1, len(nums), 2):
            result.append(nums[i])
            result.append(nums[i-1])

        return result

nums = [5,4,2,3]
x = Solution()
print(x.numberGame(nums))