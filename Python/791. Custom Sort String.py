# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
#
# Permute the characters of s so that they match the order that order was sorted.
# More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
#
# Return any permutation of s that satisfies this property.



def customSortString1(order: str, s: str) -> str:
    OurInitialStrDict = {}
    OurOrderedStr = ""
    for char in s:
        if char in OurInitialStrDict:
            OurInitialStrDict[char] += 1
        else:
            OurInitialStrDict[char] = 1

    for orderChar in order:
        while orderChar in OurInitialStrDict:
            OurOrderedStr += orderChar
            if OurInitialStrDict[orderChar] >= 2:
                OurInitialStrDict[orderChar] -= 1
            else:
                OurInitialStrDict.pop(orderChar)
                break

    if len(OurInitialStrDict) > 0:
        for key, value in OurInitialStrDict.items():
            i = 0
            while i < int(value):
                OurOrderedStr += key
                i += 1

    return OurOrderedStr

def customSortString2(order: str, s: str) -> str:
    OurInitialStrDict = {}
    OurOrderedStr = ""
    for char in s:
        if char in OurInitialStrDict:
            OurInitialStrDict[char] += 1
        else:
            OurInitialStrDict[char] = 1

    for orderChar in order:
        if orderChar in OurInitialStrDict:
            OurOrderedStr += orderChar * OurInitialStrDict[orderChar]
            OurInitialStrDict.pop(orderChar)

    if len(OurInitialStrDict) > 0:
        for key, value in OurInitialStrDict.items():
            OurOrderedStr += key * value

    return OurOrderedStr


OurOrder = "bnhgoiutrmvca"
OurS = "kajfhdglkjadbhgljkaberlgjubaldrikbgladiurgblajkrbglikuabderlgubalirbgliauderbgluibaeruigbuiarbguibarg"

print(customSortString1(OurOrder, OurS))