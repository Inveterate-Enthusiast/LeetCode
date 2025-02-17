# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.
#
# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters
# of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        set_broken = set(brokenLetters)
        t = text.split()
        result = len(t)
        for i in t:
            if len(set_broken.intersection(set(i))) >= 1:
                result -= 1

        return result

    def canBeTypedWords1(self, text: str, brokenLetters: str) -> int:
        set_broken = set(brokenLetters)
        t = text.split()
        result = len(t)
        for i in t:
            for j in i:
                if j in set_broken:
                    result -= 1
                    break
        return result

text = "leet code"
brokenLetters = "e"
x = Solution()
print(x.canBeTypedWords(text, brokenLetters))