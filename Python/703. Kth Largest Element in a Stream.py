# Design a class to find the kth largest element in a stream.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Implement KthLargest class:
#
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream
# and returns the element representing the kth largest element in the stream.
from typing import Optional, List
from collections import deque
import heapq

class KthLargest1:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


class KthLargest2:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums[:k]
        self.k = k
        heapq.heapify(self.nums)
        for i in range(k, len(nums)):
            if nums[i] > self.nums[0]:
                heapq.heappushpop(self.nums, nums[i])

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)

        return self.nums[0]



X = KthLargest2(3, [4,5,8,2])
print(X.add(3))
print(X.add(5))
print(X.add(10))
print(X.add(9))
print(X.add(4))












