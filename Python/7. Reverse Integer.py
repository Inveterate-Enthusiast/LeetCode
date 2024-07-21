# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
import math
def reverse1(x: int) -> int:
    x = list(str(x))
    OurNumber = ""
    for index in range(len(x)-1, -1, -1):
        if index == 0 and x[index] == "-":
            OurNumber = -(int(OurNumber))
            break
        OurNumber += x[index]
    OurNumber = int(OurNumber)
    xRev = math.floor(math.log2(abs(OurNumber))) if OurNumber != 0 else 0
    return OurNumber if -(32) <= xRev <= (32 - 1) else 0



x = 0
print(reverse1(x))