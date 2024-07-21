# Two strings are considered close if you can attain one from the other using the following operations:
#
# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character
# into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
#
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

def QuckSort(lst: list):
    if len(lst) <= 1:
        return
    OurLeft, OurMiddle, OurRight = [], [], []
    OurBarier = lst[0]
    for element in lst:
        if element == OurBarier:
            OurMiddle.append(element)
        elif element < OurBarier:
            OurLeft.append(element)
        else:
            OurRight.append(element)
    QuckSort(OurLeft)
    QuckSort(OurRight)
    OurI = 0
    for element in (OurLeft + OurMiddle + OurRight):
        lst[OurI] = element; OurI += 1


def closeStrings1(word1: str, word2: str) -> bool:
    OurFlag = False
    OurHash1, OurHash2 = {}, {}
    for char in word1:
        OurHash1[char] = OurHash1.get(char, 0) + 1
    for char in word2:
        OurHash2[char] = OurHash2.get(char, 0) + 1
    if OurHash1 == OurHash2:
        OurFlag = True
    else:
        OurList1 = list(OurHash1.values()); OurList2 = list(OurHash2.values())
        QuckSort(OurList1)
        QuckSort(OurList2)
        if OurList1 == OurList2:
            OurFlag = True if set(word1) == set(word2) else False
        else:
            OurFlag = False
    return OurFlag


def closeStrings2(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    OurFlag = False
    OurHash1, OurHash2 = {}, {}
    for char in word1:
        OurHash1[char] = OurHash1.get(char, 0) + 1
    for char in word2:
        OurHash2[char] = OurHash2.get(char, 0) + 1
    if OurHash1 == OurHash2:
        OurFlag = True
    else:
        OurList1 = list(OurHash1.values()); OurList2 = list(OurHash2.values())
        OurList1 = sorted(OurList1)
        OurList2 = sorted(OurList2)
        if OurList1 == OurList2:
            OurFlag = True if set(word1) == set(word2) else False
        else:
            OurFlag = False
    return OurFlag


word1 = "uau"; word2 = "ssx"
print(closeStrings2(word1, word2))