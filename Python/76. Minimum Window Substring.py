# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.

def minWindow1(s: str, t: str) -> str: #for unique characters (without dublicates)
    if len(s) == 0 or len(t):
        return ""
    elif len(s) == 1:
        if s != t:
            return ""
        else:
            return s

    OurResultString = ""
    OurDict = {}
    leftIndex = 0
    OurCurrentString = ""
    for char in t:
        if char in OurDict:
            OurDict[char] += 1
        else:
            OurDict[char] = 1

    OurCopyDict = OurDict.copy()
    for rightIndex in range(len(s)):
        OurCurrentString += s[rightIndex]
        while leftIndex <= rightIndex and not s[leftIndex] in OurDict:
            OurCurrentString = str(OurCurrentString[1:])
            leftIndex += 1
        if s[rightIndex] in OurCopyDict:
            if OurCopyDict[s[rightIndex]]>1:
                OurCopyDict[s[rightIndex]] -= 1
            else:
                OurCopyDict.pop(s[rightIndex])
        else:
            if s[rightIndex] in OurDict:
                while leftIndex < rightIndex and (s[leftIndex] != s[rightIndex] or leftIndex != rightIndex):
                    if s[leftIndex] in OurDict and s[leftIndex] != s[rightIndex]:
                        if s[leftIndex] in OurCopyDict:
                            OurCopyDict[s[leftIndex]] += 1
                        else:
                            OurCopyDict[s[leftIndex]] = 1
                    OurCurrentString = str(OurCurrentString[1:])
                    leftIndex += 1
        if OurCopyDict == {}:
            if len(OurResultString) > 0:
                OurResultString = OurCurrentString if len(OurCurrentString) < len(OurResultString) else OurResultString
            else:
                OurResultString = OurCurrentString
            while leftIndex < rightIndex and (OurCopyDict == {} or not s[leftIndex] in OurDict):
                OurCurrentString = str(OurCurrentString[1:])
                if s[leftIndex] in OurDict:
                    OurCopyDict[s[leftIndex]] = 1
                leftIndex += 1
    return OurResultString

def minWindow2(s: str, t: str) -> str:
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        if s != t:
            return ""
        else:
            return s

    OurResultString = ""
    OurDict = {}
    OurCountDict = {}
    leftIndex = 0
    OurCurrentString = ""

    for char in t:
        OurDict[char] = 0
        if not char in OurCountDict:
            OurCountDict[char] = 1
        else:
            OurCountDict[char] += 1

    OurCopyDict = OurCountDict.copy()
    for rightIndex in range(len(s)):
        OurCurrentString += s[rightIndex]

        while leftIndex < rightIndex and not s[leftIndex] in OurDict:
            OurCurrentString = str(OurCurrentString[1:])
            leftIndex += 1

        if s[rightIndex] in OurCopyDict:
            if OurCopyDict[s[rightIndex]] > 1:
                OurCopyDict[s[rightIndex]] -= 1
            else:
                OurCopyDict.pop(s[rightIndex])
            OurDict[s[rightIndex]] += 1
        elif s[rightIndex] in OurDict:
            OurDict[s[rightIndex]] += 1
            while leftIndex < rightIndex and ((s[leftIndex] in OurDict and OurDict.get(s[leftIndex]) > OurCountDict[s[leftIndex]]) or not s[leftIndex] in OurDict):
                OurCurrentString = str(OurCurrentString[1:])
                if s[leftIndex] in OurDict:
                    OurDict[s[leftIndex]] -= 1
                leftIndex += 1

        if OurCopyDict == {}:
            OurResultString = OurCurrentString if len(OurCurrentString) < len(OurResultString) or len(OurResultString) == 0 else OurResultString
            while leftIndex < rightIndex and (len(OurCopyDict) == 0 or not s[leftIndex] in OurDict or (OurDict[s[leftIndex]] > OurCountDict[s[leftIndex]])):
                OurCurrentString = str(OurCurrentString[1:])
                if s[leftIndex] in OurDict:
                    OurDict[s[leftIndex]] -= 1
                    if OurDict[s[leftIndex]] < OurCountDict[s[leftIndex]]:
                        if not s[leftIndex] in OurCopyDict:
                            OurCopyDict[s[leftIndex]] = 1
                        else:
                            OurCopyDict[s[leftIndex]] += 1
                leftIndex += 1
    return OurResultString




V = "aaabbaaba"
OurTest = "abbb"

print(minWindow2(V, OurTest))