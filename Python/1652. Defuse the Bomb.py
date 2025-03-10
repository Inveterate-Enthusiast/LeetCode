# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
#
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
#
# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
#
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        code = code if k > 0 else code[::-1]
        result = [0] * n
        for i in range(n):
            j = ((i + abs(k)) % n)
            sum_1 = sum(code[i+1:j + 1] if (i <= j) and (j < n) else code[i+1:n])
            sum_2 = sum(code[0:j + 1] if (i > j) and (j < n) else [0])
            result[i] = sum_1 + sum_2
        return result if k > 0 else result[::-1]

code = [10,5,7,7,3,2,10,3,6,9,1,6]
k = -4
x = Solution()
print(x.decrypt(code, k))