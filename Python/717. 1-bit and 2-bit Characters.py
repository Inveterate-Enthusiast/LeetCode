# We have two special characters:
#
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
from typing import List
from collections import deque

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        stack = deque()
        for bit in bits[:-1:1]:
            if stack:
                stack.pop()
            elif bit == 1:
                stack.append(bit)
        return not stack

bits = [0,1,0]
x = Solution()
print(x.isOneBitCharacter(bits))