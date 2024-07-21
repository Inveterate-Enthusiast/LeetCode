# Given two positive integers a and b, return the count of numbers having unique digits in the range [a, b] (inclusive).

def numberCount1(a: int, b: int) -> int:
    OurCount = 0
    for integer in range(a, b+1):
        OurInteger = str(integer)
        if len(OurInteger) == len(set(OurInteger)):
            OurCount += 1
    return OurCount

a = 1; b = 20
print(numberCount1(a, b))