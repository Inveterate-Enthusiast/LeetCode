# You are given an array nums of n integers and two integers k and x.
#
# The x-sum of an array is calculated by the following procedure:
#
# Count the occurrences of all elements in the array.
# Keep only the occurrences of the top x most frequent elements.
# If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
# Calculate the sum of the resulting array.
# Note that if an array has less than x distinct elements, its x-sum is the sum of the array.
#
# Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

from typing import List
from collections import defaultdict

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if n < k:
            return [sum(nums)]

        i = 0
        result = list()
        while (i + k - 1) < n:
            our_dict = defaultdict(int)
            for j in nums[i:i + k]:
                our_dict[j] += 1

            temp_list = sorted([[num, freq] for num, freq in our_dict.items()], key=lambda x: (x[1], x[0]), reverse=True)[:x]
            result.append(sum([num[0] * num[1] for num in temp_list]))
            i += 1

        return result

nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
X = Solution()
print(X.findXSum(nums, k, x))