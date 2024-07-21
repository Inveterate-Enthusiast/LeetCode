# You are given a large integer represented
# as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant
# to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.

def plusOne1(digits: list[int]) -> list[int]:
    return list(map(int, (str(int(''.join(map(str, digits)))+1))))

digits = [1,2,3]
print(plusOne1(digits))

V = [1,2,3]
T = list(map(int, (str(int(''.join(map(str, V)))+1))))
print(T)
