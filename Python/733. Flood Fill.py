# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].
#
# To perform a flood fill:
#
# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically)
# and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.
from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        rows, columns = len(image), len(image[0])
        our_set = set()
        original_color = image[sr][sc]
        queue.append((sr, sc))
        adjacent_coord = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while queue:
            r, c = queue.popleft()
            our_set.add((r, c))

            for i, j in adjacent_coord:
                r_adj, c_adj = (r + i), (c + j)
                if r_adj < 0 or c_adj < 0:
                    continue
                elif r_adj < rows and c_adj < columns and image[r_adj][c_adj] == original_color and not (r_adj, c_adj) in our_set:
                    queue.append((r_adj, c_adj))
            image[r][c] = color
        return image

    def floodFill1(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        rows, columns = len(image), len(image[0])
        queue.append((sr, sc))
        original_color = image[sr][sc]
        adjacent_coord = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while queue:
            r, c = queue.popleft()
            image[r][c] = color

            for i, j in adjacent_coord:
                r_adj, c_adj = (r + i), (c + j)
                if r_adj < 0 or c_adj < 0:
                    continue
                elif r_adj < rows and c_adj < columns and image[r_adj][c_adj] == original_color and image[r_adj][c_adj] != color:
                    queue.append((r_adj, c_adj))
        return image

image = [[0,0,0],[0,0,0]]; sr = 0; sc = 0; color = 0
x = Solution()
print(x.floodFill1(image, sr, sc, color))