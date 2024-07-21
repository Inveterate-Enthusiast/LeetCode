# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord1(s: str) -> int:
    return len(s.split()[-1])

s = "   fly me   to   the moon  "
print(lengthOfLastWord1(s))