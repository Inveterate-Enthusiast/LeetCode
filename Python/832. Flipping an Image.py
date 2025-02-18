# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.
#
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
#
# For example, inverting [0,1,1] results in [1,0,0].

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        r, c = len(image), len(image[0])
        result = [[None] * c for i in range(r)]
        for row in range(r):
            for col, i in enumerate(image[row][::-1]):
                result[row][col] = i^1
        return result


image = [[1,1,0],[1,0,1],[0,0,0]]
x = Solution()
print(x.flipAndInvertImage(image))