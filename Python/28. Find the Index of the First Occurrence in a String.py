# Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr1(haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
        return -1
    OurPrefFun = [0] * len(needle)
    i, j = 1, 0
    while i < len(needle):
        if needle[i] == needle[j]:
            OurPrefFun[i] = j+1
            i += 1; j += 1
        else:
            if j > 0:
                j = OurPrefFun[j-1]
            else:
                i += 1

    i = j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            if j == (len(needle)-1):
                # подумать
                return i - (len(needle)-1)
            else:
                i += 1; j += 1
        else:
            if j > 0:
                j = OurPrefFun[j-1]
            else:
                i += 1
    return -1

haystack = "leetcode"; needle = "leeto"
print(strStr1(haystack, needle))