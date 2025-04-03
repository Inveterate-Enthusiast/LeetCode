# You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive
# (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.
#
# Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.
#
# Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.

from collections import defaultdict

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        our_dict = defaultdict(int)
        result = 0
        for i in range(lowLimit, (highLimit + 1)):
            box = sum([int(j) for j in str(i)])
            our_dict[box] += 1
            result = max(our_dict[box], result)
        return result

lowLimit = 1
highLimit = 10
x = Solution()
print(x.countBalls(lowLimit, highLimit))