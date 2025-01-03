# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average
# of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother).
# If one or more of the surrounding cells of a cell is not present, we do not consider it in the average
# (i.e., the average of the four cells in the red smoother).
from typing import List

class Solution:
    def round(self, img, row, col, len_row, len_col) -> int:
        our_sum = 0
        our_count = 0
        for i in range(-1, 1+1, 1):
            for j in range(-1, 1+1, 1):
                n = row + i; m = col + j
                if (0 <= n < len_row) and (0 <= m < len_col):
                    our_sum += img[row + i][col + j]
                    our_count += 1
        return our_sum // our_count


    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        len_row = len(img)
        len_col = len(img[0])
        result = [[None] * len_col for i in range(len_row)]

        for row in range(len(img)):
            for col in range(len(img[row])):
                result[row][col] = self.round(img, row, col, len_row, len_col)
        return result

img = [[100,200,100],[200,50,200],[100,200,100]]
x = Solution()
print(x.imageSmoother(img))