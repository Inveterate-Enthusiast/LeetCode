# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.

def mergeAlternately1(word1: str, word2: str) -> str:
    OurResultString = ""
    Letter1 = 0
    Letter2 = 0
    for index in range(len(word1) + len(word2)):
        if (index == 0 or Letter2 == (len(word2)) or index % 2 == 0) and Letter1 != (len(word1)):
            OurResultString += word1[Letter1]
            Letter1 += 1
        elif (Letter1 == (len(word1)) or index % 2 != 0) and Letter2 != (len(word2)):
            OurResultString += word2[Letter2]
            Letter2 += 1
    return OurResultString


def mergeAlternately2(word1: str, word2: str) -> str:
    OurResultString = ""
    OurL1 = OurL2 = index = 0
    while OurL1 < len(word1) and OurL2 < len(word2):
        if index %2 == 0:
            OurResultString += word1[OurL1]; OurL1 += 1
            index += 1
        else:
            OurResultString += word2[OurL2]; OurL2 += 1
            index += 1
    while OurL1 < len(word1):
        OurResultString += word1[OurL1]; OurL1 += 1
    while OurL2 < len(word2):
        OurResultString += word2[OurL2]; OurL2 += 1

    return OurResultString


OurWord1 = "ab"
OurWord2 = "pqrs"
print(mergeAlternately2(OurWord1, OurWord2))