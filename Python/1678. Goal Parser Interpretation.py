# You own a Goal Parser that can interpret a string command.
# The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
# The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
# The interpreted strings are then concatenated in the original order.
#
# Given the string command, return the Goal Parser's interpretation of command.


class Solution:
    def interpret(self, command: str) -> str:
        return (command.replace("()", "o")).replace("(al)", "al")

    def interpret1(self, command: str) -> str:
        result = str()
        temp = str()
        for char in command:
            if char == "G":
                result += char
                temp = str()
            else:
                temp += char

            if temp == "()" or temp == "(al)":
                result += ("o" if temp == "()" else "al")
                temp = str()
        return result

command = "G()(al)"
x = Solution()
print(x.interpret1(command))