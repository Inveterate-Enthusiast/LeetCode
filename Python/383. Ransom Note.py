# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.




class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rDict = {i: ransomNote.count(i) for i in set(ransomNote)}
        mDict = {i: magazine.count(i) for i in set(magazine)}

        for char, count in rDict.items():
            if char not in mDict or count > mDict[char]:
                return False

        return True




ransomNote = "aa"; magazine = "ab"
X = Solution()
print(X.canConstruct(ransomNote, magazine))


