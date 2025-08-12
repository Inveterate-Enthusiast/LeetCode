# You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.
#
# You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes.
# Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits.
# The final digits are then grouped as follows:
#
# 2 digits: A single block of length 2.
# 3 digits: A single block of length 3.
# 4 digits: Two blocks of length 2 each.
# The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most two blocks of length 2.
#
# Return the phone number after formatting.

class Solution:
    def reformatNumber(self, number: str) -> str:
        number_2 = (number.replace(" ", "")).replace("-", "")
        result = str()
        cnt = 0
        n = len(number_2)
        for i in range(n):
            if ((rem := (n - i)) <= 4) and cnt == 0:
                if rem <= 3:
                    result += number_2[i:]
                else:
                    result += (number_2[i: (i + 1 + 1)] + "-" + number_2[(i + 2):])
                break

            cnt += 1
            result += number_2[i]
            if cnt == 3:
                result += ("-" if i < (n - 1) else "")
                cnt = 0

        return result

number = "1-23-45 6"
x = Solution()
print(x.reformatNumber(number))