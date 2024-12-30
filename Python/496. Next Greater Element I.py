# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
#
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element
# of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
#
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
from typing import List
from collections import deque, defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        our_dict = defaultdict(lambda: -1)
        our_stack = deque()
        for num in nums2:
            while our_stack and num > our_stack[-1]:
                our_dict[our_stack.pop()] = num
            our_stack.append(num)

        for num in nums1:
            result.append(our_dict[num])
        return result

nums1 = [4,1,2]; nums2 = [1,3,4,2]
x = Solution()
print(x.nextGreaterElement(nums1, nums2))