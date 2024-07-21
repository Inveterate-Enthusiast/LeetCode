# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately,
# but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.

def compress1(chars: list[str]) -> int:
    OurCompress = []
    CurrentChar = ""
    OurCount = 0
    for index in range(len(chars)):
        if index == (len(chars) - 1) and CurrentChar == chars[index]:
            OurCount += 1
            if OurCount > 1:
                OurCompress.extend(i for i in str(OurCount))

        if chars[index] != CurrentChar:
            if OurCount > 1:
                OurCompress.extend(i for i in str(OurCount))
            if chars[index] != CurrentChar:
                CurrentChar = chars[index]
                OurCompress.append(CurrentChar)
                OurCount = 1
        else:
            OurCount += 1


    chars[:] = OurCompress
    return len(OurCompress)

OurChars = ["a","a","b","b","c","c","c"]
print(compress1(OurChars))
print(OurChars)