# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

def longestCommonPrefix1(strs: list[str]) -> str:
    if len(strs) < 2:
        return strs[0]
    OurMinIndex = 0
    for index in range(len(strs)):
        if len(strs[index]) < len(strs[OurMinIndex]):
            OurMinIndex = index
    OurLongestPrefix = strs[OurMinIndex]
    for StrIndex in range(len(strs)):
        if StrIndex == OurMinIndex:
            continue
        for letterIndex in range(len(OurLongestPrefix)):
            if letterIndex > (len(strs[StrIndex])-1):
                break
            elif OurLongestPrefix[letterIndex] != strs[StrIndex][letterIndex]:
                OurLongestPrefix = OurLongestPrefix[:letterIndex]
                break
    return OurLongestPrefix


OurStrs = ["ab", "a"]
print(longestCommonPrefix1(OurStrs))