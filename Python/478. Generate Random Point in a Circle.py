# Given the radius and the position of the center of a circle,
# implement the function randPoint which generates a uniform random point inside the circle.
#
# Implement the Solution class:
#
# Solution(double radius, double x_center, double y_center) initializes the object
# with the radius of the circle radius and the position of the center (x_center, y_center).
# randPoint() returns a random point inside the circle. A point on the circumference
# of the circle is considered to be in the circle. The answer is returned as an array [x, y].
import numpy as np
import math
import random
from typing import List, Optional

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.__radius = radius
        self.__y_center = y_center
        self.__x_center = x_center

    def randPoint(self) -> List[float]:
        random_radius = self.__radius * math.sqrt(random.random())
        random_angle = 2 * math.pi * random.random()
        x = self.__x_center + random_radius * math.cos(random_angle)
        y = self.__y_center + random_radius * math.sin(random_angle)
        return [x, y]



X = Solution(1.0, 0.0, 0.0)
print(X.randPoint())
print(X.randPoint())
print(X.randPoint())