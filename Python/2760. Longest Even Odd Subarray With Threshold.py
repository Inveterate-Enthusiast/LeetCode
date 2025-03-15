# You are given a 0-indexed integer array nums and an integer threshold.
#
# Find the length of the longest subarray of nums starting at index l and ending
# at index r (0 <= l <= r < nums.length) that satisfies the following conditions:
#
# nums[l] % 2 == 0
# For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
# For all indices i in the range [l, r], nums[i] <= threshold
# Return an integer denoting the length of the longest such subarray.
#
# Note: A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        left, result = 0, 0
        n = len(nums)

        for right in range(n):
            if nums[right] > threshold:
                left = right + 1
                continue

            while left < n and nums[left] % 2 != 0 and nums[left] <= threshold:
                left += 1
            else:
                if left == n: return result

            if right != 0 and (nums[right] % 2) != (nums[right - 1] % 2):
                result = max(result, (right - left + 1))
            else:
                left = right
                if (nums[right] % 2) == 0: result = max(result, 1)

        return result

nums = [10,1,10]
threshold = 3
x = Solution()
print(x.longestAlternatingSubarray(nums, threshold))