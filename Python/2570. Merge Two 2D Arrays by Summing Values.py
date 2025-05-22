# You are given two 2D integer arrays nums1 and nums2.
#
# nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# Each array contains unique ids and is sorted in ascending order by id.
#
# Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
#
# Only ids that appear in at least one of the two arrays should be included in the resulting array.
# Each id should be included only once and its value should be the sum of the values of this id in the two arrays.
# If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
# Return the resulting array. The returned array must be sorted in ascending order by id.

from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = list()
        i1, i2 = 0, 0
        len1, len2 = len(nums1), len(nums2)
        while (i1 < len1) or (i2 < len2):
            temp1 = nums1[i1] if i1 < len1 else None
            temp2 = nums2[i2] if i2 < len2 else None
            if (temp1 is None) or (not temp1 is None and not temp2 is None and temp2[0] < temp1[0]):
                result.append(temp2)
                i2 += 1
            elif (temp2 is None) or (not temp2 is None and not temp1 is None and temp1[0] < temp2[0]):
                result.append(temp1)
                i1 += 1
            else:
                result.append([temp1[0], temp1[1] + temp2[1]])
                i1, i2 = i1 + 1, i2 + 1

        return result

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
x = Solution()
print(x.mergeArrays(nums1, nums2))