# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
from typing import List
from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        our_dict = defaultdict(int)
        our_max = 0
        for num in nums:
            our_dict[num]= our_dict.get(num, 0) + 1
            our_max = max(our_max, our_dict[num])

        our_dict = defaultdict(int)
        cur_max = 0
        min_length = float("inf")
        left = right = 0
        while left <= right < len(nums):
            our_dict[nums[right]] = our_dict.get(nums[right], 0) + 1
            cur_max = max(cur_max, our_dict[nums[right]])

            while cur_max == our_max:
                min_length = min(min_length, right - left + 1)
                our_dict[nums[left]] = our_dict.get(nums[left], 0) - 1
                if nums[left] == nums[right]: cur_max -= 1
                left += 1

            right += 1

        return min_length

nums = [1,2,2,3,1]
x = Solution()
print(x.findShortestSubArray(nums))