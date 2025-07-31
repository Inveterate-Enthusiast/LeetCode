# Your friend is typing his name into a keyboard. Sometimes, when typing a character c,
# the key might get long pressed, and the character will be typed 1 or more times.
#
# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name,
# with some characters (possibly none) being long pressed.

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0] or name[-1] != typed[-1]:
            return False

        i = j = 0
        temp, count_origin, count_typed = name[i], 0, 0
        n, m = len(name), len(typed)
        while i < n:
            if temp == name[i]:
                count_origin += 1

            if i == (n - 1) or temp != name[i]:
                if j >= m or temp != typed[j]:
                    return False
                else:
                    count_typed = 0
                while j < m and typed[j] == temp:
                    j += 1
                    count_typed += 1
                if count_typed < count_origin:
                    return False

                temp = name[i]
                count_origin = 1
            i += 1

        while j < m:
            if typed[j] != temp:
                return False
            j += 1

        return True




name = "vtkgn"
typed = "vttkgnn"
x = Solution()
print(x.isLongPressedName(name, typed))