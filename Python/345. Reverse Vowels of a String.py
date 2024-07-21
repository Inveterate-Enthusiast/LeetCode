# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# first we have to know, if here is a vowel charachter
def CheckVowel(letter: str) -> bool:
    OurVowels = "aeiouyAEIOUY"
    if letter.isalpha() and letter in OurVowels:
        OurFlag = True
    else:
        OurFlag = False
    return OurFlag

def reverseVowels1(s: str) -> str:
    if len(s) <= 1:
        return s
    s = list(s)
    OurVowelsList = []
    for char in s:
        if CheckVowel(char):
            OurVowelsList.append(char)
    i = 0
    for index in range(len(s)):
        if CheckVowel(s[index]):
            s[index] = OurVowelsList[-i-1]
            i += 1

    return "".join(s)


def reverseVowels2(s: str) -> str:
    if len(s) <= 1:
        return s
    s = list(s)
    OurVowels = "aeiouAEIOU"
    OurVowelsList = []
    for char in s:
        if char.isalpha() and char in OurVowels:
            OurVowelsList.append(char)
    i = 0
    for index in range(len(s)):
        if s[index].isalpha() and s[index] in OurVowels:
            s[index] = OurVowelsList[-i-1]
            i += 1

    return "".join(s)



OurStr = "Yo! Bottoms up, U.S. Motto, boy!"

print(reverseVowels2(OurStr))