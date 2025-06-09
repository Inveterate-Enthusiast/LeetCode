# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

from typing import List
from collections import defaultdict
import numpy as np

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        our_dict = defaultdict(int)
        for i in nums:
            our_dict[i] += 1

        n = len(nums)
        result = list()
        for num, freq in our_dict.items():
            if freq > np.floor(n / 3):
                result.append(num)

        return result

    def majorityElement1(self, nums: List[int]) -> List[int]: # didn't pass all test cases
        our_max = max(nums)
        n = len(nums)
        our_list = [0] * (our_max + 1)
        for i in nums:
            our_list[i] += 1

        result = list()
        for num, freq in enumerate(our_list):
            if freq > np.floor(n / 3):
                result.append(num)

        return result

    def majorityElement2(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        n = len(nums)
        result = list()
        temp = float("inf")
        freq = 0
        for num in sorted_nums:
            if num != temp:
                temp = num
                freq = 0
            freq += 1
            if (freq > np.floor(n / 3)) and ((not result) or (num != result[-1])):
                result.append(num)
        else:
            if (freq > np.floor(n / 3)) and ((not result) or (num != result[-1])):
                result.append(num)

        return result

    def majorityElement3(self, nums: List[int]) -> List[int]: # didn't pass all test cases
        return [i for i in set(nums) if nums.count(i) > (len(nums) // 3)]

    def majorityElement4(self, nums: List[int]) -> List[int]:
        num1, num2 = None, None
        freq1, freq2 = 0, 0
        for num in nums:
            if num == num1:
                freq1 += 1
            elif num == num2:
                freq2 += 1
            elif freq1 == 0:
                num1, freq1 = num, 1
            elif freq2 == 0:
                num2, freq2 = num, 1
            else:
                freq1, freq2 = (freq1 - 1), (freq2 - 1)

        freq1, freq2 = 0, 0
        for num in nums:
            if num == num1:
                freq1 += 1
            elif num == num2:
                freq2 += 1

        return [num[0] for num in ((num1, freq1), (num2, freq2)) if num[1] > (len(nums) // 3)]


nums = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
x = Solution()
print(x.majorityElement4(nums))