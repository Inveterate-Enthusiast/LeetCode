# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.
# If there are duplicates in arr, count them separately.

from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        our_set = set()
        for i in arr:
            our_set.add(i)

        result = 0
        for i in arr:
            if (i + 1) in our_set:
                result += 1
        return result


arr = [1,2,3]
x = Solution()
print(x.countElements(arr))