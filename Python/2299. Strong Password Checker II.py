# A password is said to be strong if it satisfies all the following criteria:
#
# It has at least 8 characters.
# It contains at least one lowercase letter.
# It contains at least one uppercase letter.
# It contains at least one digit.
# It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
# It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
# Given a string password, return true if it is a strong password. Otherwise, return false.

from functools import reduce

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        list_check = [0] * 5
        n = len(password)
        if n >= 8:
            list_check[0] = 1

        our_set = {i for i in "!@#$%^&*()-+"}
        for i in range(n):
            if password[i].isalpha():
                if password[i].islower():
                    list_check[1] = 1
                elif password[i].isupper():
                    list_check[2] = 1
            elif password[i].isdigit():
                list_check[3] = 1
            elif password[i] in our_set:
                list_check[4] = 1

            if i > 0 and password[i] == password[i - 1]:
                return False

        return bool(reduce(lambda acc, x: acc * x, list_check, 1))


password = "IloveLe3tcode!"
x = Solution()
print(x.strongPasswordCheckerII(password))