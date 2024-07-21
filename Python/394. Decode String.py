# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets
# is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid;
# there are no extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain
# any digits and that digits are only for those repeat numbers, k.
# For example, there will not be input like 3a or 2[4].
#
# The test cases are generated so that the length of the output will never exceed 105.

def decodeString1(s: str) -> str:
    OurDecodeStr = ""
    for index in range(len(s)):
        if s[index].isdigit():
            OurDecodeStr += ("+" if index != 0 and (s[index-1] == "]" or s[index-1].isalpha()) else "") + s[index]
        elif s[index] == "[":
            OurDecodeStr += "*("
        elif s[index] == "]":
            OurDecodeStr += ")"
        elif s[index].isalpha():
            OurDecodeStr += ("+" if index != 0 and (s[index-1] == "]" or s[index-1].isalpha()) else "") + "\"" + s[index] + "\""
    return eval(OurDecodeStr)

s = "22[abc]3[cd]ef"
print(decodeString1(s))