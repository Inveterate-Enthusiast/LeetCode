# You are given a positive integer num.
# You may swap any two digits of num that have the same parity
# (i.e. both odd digits or both even digits).
#
# Return the largest possible value of num after any number of swaps.

class Solution:
    def largestInteger(self, num: int) -> int:
        l_odd, l_even = list(), list()
        l_num = [int(i) for i in str(num)]
        for n in l_num:
            if (n % 2) == 0:
                l_even.append(n)
            else:
                l_odd.append(n)

        l_odd.sort(); l_even.sort()
        result = 0
        for n in l_num:
            if (n % 2) == 0:
                result = (result * 10) + l_even.pop()
            else:
                result = (result * 10) + l_odd.pop()

        return result


num = 65875
x = Solution()
print(x.largestInteger(num))