# You are given a positive integer num consisting of exactly four digits.
# Split num into two new integers new1 and new2 by using the digits found in num.
# Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.
#
# For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3.
# Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
# Return the minimum possible sum of new1 and new2.

class Solution:
    def minimumSum(self, num: int) -> int:
        num_new = sorted([i for i in str(num)])
        return int(num_new[0] + num_new[2]) + int(num_new[1] + num_new[3])

num = 2932
x = Solution()
print(x.minimumSum(num))