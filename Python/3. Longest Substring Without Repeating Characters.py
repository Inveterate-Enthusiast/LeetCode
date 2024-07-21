def lengthOfLongestSubstring1(s:str) -> int:
    if len(s) == 1 or len(s) == 0:
        return 1 if len(s) == 1 else 0
    else:
        count, finalCount = 0, 0
        listChar = []

        for indexStart in range(len(s)):
            for index in range(indexStart, len(s)):
                listChar.append(s[index])
                if len(listChar) == len(list(set(listChar))):
                    count += 1
                else:
                    finalCount = count if count > finalCount else finalCount
                    count = 0
                    listChar = []
                    break
    return finalCount

def lengthOfLongestSubstring2(s:str) -> int:
    if len(s) == 1 or len(s) == 0:
        return 1 if len(s) == 1 else 0
    finalCount, count = 0, 0
    lengthList = []
    for index in range(len(s)):
        lengthList.append((s[index+1:].find(s[index])))
    for i in range(len(lengthList)):
        if lengthList[i] == (-1):
            count += 1
        else:
            finalCount = count+1 if count > finalCount else finalCount
            count = 0
    finalCount = count if count > finalCount else finalCount
    return finalCount if finalCount != 0 else len(s)


def lengthOfLongestSubstring(s:str) -> int:
    finalCount, start = 0, 0
    lookup = {}
    for i, char in enumerate(s):
        if char in lookup and start <= lookup[char]:
            start = lookup[char] + 1
        else:
            finalCount = max(finalCount, i - start + 1)
        lookup[char] = i
    return finalCount



s = "abcbsdar"

N = lengthOfLongestSubstring(s)
print(N)

def le(s:str) -> int:
    start, knownDict = 0, {}
    finalCount = 0
    for i, char in enumerate(s):
        if char in knownDict and start <= knownDict[char]:
            start = knownDict[char] + 1
        else:
            finalCount = max(finalCount, i - start + 1)
        knownDict[char] = i
    return finalCount

M = le(s)
print(M)