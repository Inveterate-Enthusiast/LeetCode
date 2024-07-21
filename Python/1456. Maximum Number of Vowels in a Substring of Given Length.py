# Given a string s and an integer k,
# return the maximum number of vowel letters in any substring of s with length k.
#
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

def maxVowels1(s: str, k: int) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    OurVowelsDict = {}
    for char in vowels:
        OurVowelsDict[char] = 1
    leftIndex = CurrentNumber = 0
    ResultNumber = None
    currentStr = ""
    for rightIndex in range(len(s)):
        currentStr += s[rightIndex]
        CurrentNumber = (CurrentNumber + 1) if s[rightIndex] in OurVowelsDict else CurrentNumber
        if (rightIndex - leftIndex + 1) < k:
            continue
        while leftIndex <= rightIndex and (rightIndex - leftIndex + 1) > k:
            currentStr = str(currentStr[1:])
            CurrentNumber = (CurrentNumber - 1) if s[leftIndex] in OurVowelsDict else CurrentNumber
            leftIndex += 1
        if (rightIndex - leftIndex + 1) == k:
            ResultNumber = max(ResultNumber, CurrentNumber) if ResultNumber else CurrentNumber
    return ResultNumber


# Попытаемся сократить время работы функции
def maxVowels2(s: str, k: int) -> int:
    ResultNumber = CurrentNumber = 0
    OurVowelsSet = set(['a', 'e', 'i', 'o', 'u'])
    for index, char in enumerate(s):
        if char in OurVowelsSet:
            CurrentNumber += 1
        if (index-k) >= 0 and s[index-k] in OurVowelsSet:
            CurrentNumber -= 1
        ResultNumber = max(ResultNumber, CurrentNumber)
    return ResultNumber


s = "abciiidef"; k = 3
print(maxVowels2(s, k))