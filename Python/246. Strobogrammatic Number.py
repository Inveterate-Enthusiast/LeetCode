# Given a string num which represents an integer, return true if num is a strobogrammatic number.
#
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        our_dict = {
            "0": "0",
            "1": "1",
            "8": "8",
            "6": "9",
            "9": "6"
        }
        left, right = 0, (len(num) - 1)
        while left <= right:
            if not num[left] in our_dict:
                return False
            if num[left] in our_dict and our_dict[num[left]] != num[right]:
                return False
            left += 1; right -= 1
        return True

num = "69"
x = Solution()
print(x.isStrobogrammatic(num))