# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
#
# It has a length of k.
# It is a divisor of num.
# Given integers num and k, return the k-beauty of num.
#
# Note:
#
# Leading zeros are allowed.
# 0 is not a divisor of any value.
# A substring is a contiguous sequence of characters in a string.

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_s = str(num)
        result = 0
        for i in range(k-1, len(num_s)):
            n = (int(num_s[i-k+1:i+1]))
            if n and (num % n) == 0:
                result += 1
        return result

num = 430043
k = 2
x = Solution()
print(x.divisorSubstrings(num, k))