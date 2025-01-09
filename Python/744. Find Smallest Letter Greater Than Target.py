# You are given an array of characters letters that is sorted in non-decreasing order,
# and a character target. There are at least two different characters in letters.
#
# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, (len(letters) - 1)
        result = None
        while left <= right:
            mid = (right + left) // 2
            if letters[mid] > target:
                result = min(result, letters[mid]) if result else letters[mid]
                right = mid - 1
            elif letters[mid] <= target:
                left = mid + 1

        return result if result else letters[0]

letters = ["x","x","y","y"]; target = "z"
x = Solution()
print(x.nextGreatestLetter(letters, target))