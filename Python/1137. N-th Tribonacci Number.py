# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.

def tribonacci1(n: int) -> int:
    if n <= 1:
        return n
    OurList = [0, 1] + ([0] * (n-1))
    for index in range(2, len(OurList)):
        OurList[index] = (OurList[index-3] if (index-3) >= 0 else 0) + (OurList[index-2] if (index-2) >= 0 else 0) + (OurList[index-1] if (index-1) >= 0 else 0)
    return OurList[-1]
OurN = 4
print(tribonacci1(OurN))