# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded back to the original list of strings.
from typing import Optional, List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans_str = str()
        for string in strs:
            ans_str += str(len(string)) + "|" + string
        return ans_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        s = list(s[::-1]); cur_str = str()
        cur_num = 0; ans_list = list()
        while s:
            while s[-1] != "|":
                cur_num = cur_num * 10 + int(s.pop())
            else:
                cur_str = str()
                s.pop()

            for _ in range(cur_num):
                cur_str += s.pop()
            else:
                ans_list.append(cur_str)
                cur_num = 0
        return ans_list


X = Codec()
print(a := ["p", "|"])
print(a := X.encode(a))
print(X.decode(a))
