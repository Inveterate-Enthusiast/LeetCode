# You are given a string s, which contains stars *.
#
# In one operation, you can:
#
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
#
# Note:
#
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.


def removeStars1(s: str) -> str:
    OurStar = "*"
    index = s.find(OurStar)
    while index > 0:
        OurBeforeString = s[:index-1] if index > 0 else s[:index]
        OurAfterString = s[index+1:] if index < len(s) else ""
        s = OurBeforeString + OurAfterString
        index = s.find(OurStar)
    return s

def removeStars2(s: str) -> str:
    OurStar = "*"
    OurPopList = []
    for index in range(len(s)):
        if s[index] == OurStar:
            OurPopList.append(index)
    i = 0
    for indexValue in OurPopList:
        OurBeforeStr = s[:indexValue-1-i] if (indexValue-i) > 0 else s[:indexValue-i]
        OurAfterStr = s[indexValue-i+1:] if (indexValue-i) < len(s) else ""
        s = OurBeforeStr + OurAfterStr
        i += 2
    return s


def removeStars3(s: str) -> str:
    OurStack = []
    for char in s:
        if char == "*":
            OurStack.pop()
        else:
            OurStack.append(char)
    s = "".join(OurStack)
    return s

s = "leet**cod*e"
print(removeStars3(s))
