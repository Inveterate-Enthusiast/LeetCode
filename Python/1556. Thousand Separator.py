# Given an integer n, add a dot (".") as the thousands separator and return it in string format.

class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)

        result = str()
        nn = str(n)
        cnt = 0
        for i in range(len(nn) - 1, -1, -1):
            cnt += 1
            if cnt <= 3:
                temp = str()
            else:
                temp = "."; cnt = 1

            result = nn[i] + temp + result

        return result

n = 51040
x = Solution()
print(x.thousandSeparator(n))