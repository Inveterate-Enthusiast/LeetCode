# For two strings s and t, we say "t divides s"
# if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
import math
def gcdOfStrings1(str1: str, str2: str) -> str:
    OurGCD = ""
    OurLargestDict = {}
    OurMinDict = {}
    for char in (str1 if len(str1) >= len(str2) else str2):
        if not char in OurLargestDict:
            OurLargestDict[char] = 1
        else:
            OurLargestDict[char] += 1

    for char in (str2 if len(str2) <= len(str1) else str1):
        if char in OurLargestDict:
            OurGCD += char

    return OurGCD


def gcdOfStrings2(str1: str, str2: str) -> str: # поиск НАИМЕНЬШЕГО общего делителя в строках. Наибольший ищется по-другому
    OurGCD = ""
    OurCurrentString = ""
    OurStr = str2 if len(str2) <= len(str1) else str1
    OurGeneralStr = str1 if len(str1) >= len(str2) else str2
    OurFlag = False
    i = 0
    while i <= len(OurStr)-1 and not OurFlag:
        OurCurrentString += OurStr[i]
        if len(set(OurCurrentString)) == len(set(OurStr)):
            OurFlag = True
            for index in range(0, len(OurStr), len(OurCurrentString)):
                if not OurStr[index:(index+len(OurCurrentString))] == OurStr[(len(OurStr) - len(OurCurrentString)-index) : ((len(OurStr) - len(OurCurrentString)-index) + len(OurCurrentString))]:
                    OurFlag = False
                    break
        i += 1
    OurFlag = True
    for index in range(0, len(OurGeneralStr), len(OurCurrentString)):
        if not OurGeneralStr[index : index + len(OurCurrentString)] == OurCurrentString:
            OurFlag = False
            break

    if OurFlag:
        OurGCD = OurCurrentString

    return OurGCD

def gcdOfStrings3(str1: str, str2: str) -> str: # Это гениальное решение НОД для строк
    if (str1 + str2) != (str2 + str1):
        return ""
    else:
        return str1[:math.gcd(len(str1), len(str2))]

str1 = "ABABABAB"
str2 = "ABAB"
print(gcdOfStrings3(str1, str2))