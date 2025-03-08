# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        our_dict = {
            "I": [1, set(["V", "X"])],
            "V": [5, set([])],
            "X": [10, set(["L", "C"])],
            "L": [50, set([])],
            "C": [100, set(["D", "M"])],
            "D": [500, set([])],
            "M": [1000, set([])]
        }
        min_set = {"I", "X", "C"}
        result = list()
        temp = 0
        prev = 0
        n = len(s)
        for i in range(n):
            if s[i] in min_set:
                if (i + 1) < n and s[i + 1] in our_dict[s[i]][1]:
                    temp = our_dict[s[i]][0]
                else:
                    if s[i] == prev:
                        if result:
                            result[-1] += our_dict[s[i]][0]
                        else:
                            result.append(our_dict[prev][0] + our_dict[s[i]][0])
                    else:
                        result.append(our_dict[s[i]][0] - temp)
                        temp = 0
            else:
                result.append(our_dict[s[i]][0] - temp)
                temp = 0
            prev = s[i]
        return sum(result)

    def romanToInt1(self, s: str) -> int:
        our_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        prev = 0
        for i in range(len(s) - 1, -1, -1):
            v = our_dict[s[i]]
            if v < prev:
                result -= v
            else:
                result += v
            prev = v
        return result


s = "III"
X = Solution()
print(X.romanToInt(s))