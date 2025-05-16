# You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line.
# For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.
#
# Return the number of integer points on the line that are covered with any part of a car.

from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        our_set = set()
        for start, end in nums:
            our_set = our_set.union(set([i for i in range(start, end+1)]))

        return len(our_set)

    def numberOfPoints1(self, nums: List[List[int]]) -> int:
        nums_sort = sorted(nums, key=lambda x: (x[0], x[1]))
        left_temp, right_temp = nums_sort[0][0], nums_sort[0][1]
        our_set = set()
        for left, right in nums_sort[1:]:
            if right_temp < left:
                our_set = our_set.union(set([i for i in range(left_temp, right_temp+1)]))
                left_temp, right_temp = left, right
            else:
                right_temp = max(right_temp, right)
        else:
            our_set = our_set.union(set([i for i in range(left_temp, right_temp+1)]))

        return len(our_set)

    def numberOfPoints2(self, nums: List[List[int]]) -> int:
        nums_sort = sorted(nums, key=lambda x: (x[0], x[1]))
        left_temp, right_temp = nums_sort[0][0], nums_sort[0][1]
        result = 0
        for left, right in nums_sort[1:]:
            if right_temp < left:
                result += (right_temp - left_temp + 1)
                left_temp, right_temp = left, right
            else:
                right_temp = max(right_temp, right)
        else:
            result += (right_temp - left_temp + 1)

        return result

nums = [[3,6],[1,5],[4,7]]
x = Solution()
print(x.numberOfPoints1(nums))