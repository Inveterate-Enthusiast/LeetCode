# You are given a string s and an array of strings words. All the strings of words are of the same length.
#
# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
#
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

def findSubstring1(s: str, words: list[str]) -> list[int]:
    OurWordsStr = str("".join(words))
    if len(s) < len(OurWordsStr):
        return []

    OurWordsDict = {}
    for word in words:
        if not word in OurWordsDict:
            OurWordsDict[word] = 1
        else:
            OurWordsDict[word] += 1

    OurIndices = []
    leftIndex = 0
    OurCurrentString = ""
    for rightIndex in range(len(s)):
        OurCurrentString += s[rightIndex]
        if leftIndex <= rightIndex and len(s[leftIndex:rightIndex+1]) < len(OurWordsStr):
            continue
        while leftIndex <= rightIndex and len(s[leftIndex:rightIndex+1]) > len(OurWordsStr):
            OurCurrentString = str(OurCurrentString[1:])
            leftIndex += 1

        OurCurrentDict = OurWordsDict.copy()
        OurTrue = True
        for index in range(0, len(OurCurrentString), len(words[0])):
            OurCurrentWord = OurCurrentString[index:index + len(words[0])]
            if not OurCurrentWord in OurCurrentDict:
                OurTrue = False
                break
            else:
                if OurCurrentDict[OurCurrentWord] == 1:
                    OurCurrentDict.pop(OurCurrentWord)
                else:
                    OurCurrentDict[OurCurrentWord] -= 1
        if OurTrue:
            OurIndices.append(leftIndex)

    return OurIndices

V = "barfoothefoobarman"
OurWords = ["foo","bar"]

print(findSubstring1(V, OurWords))