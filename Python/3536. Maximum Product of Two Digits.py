# You are given a positive integer n.
#
# Return the maximum product of any two digits in n.
#
# Note: You may use the same digit twice if it appears more than once in n.

class Solution:
    def maxProduct(self, n: int) -> int:
        our_list = sorted([i for i in str(n)], reverse=True)
        return int(our_list[0]) * int(our_list[1])

    def maxProduct1(self, n: int) -> int:
        n1, n2 = float("-inf"), float("-inf")
        while n > 0:
            temp = n % 10
            if temp > n1:
                n2, n1 = n1, temp
            elif temp > n2:
                n2 = temp
            n = n // 10

        return n1 * n2

n = 31
x = Solution()
print(x.maxProduct1(n))