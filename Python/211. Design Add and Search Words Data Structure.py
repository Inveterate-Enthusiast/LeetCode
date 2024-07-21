# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
# word may contain dots '.' where dots can be matched with any letter.
from collections import deque


class Trie:
    class TrieNode:
        def __init__(self, next=None, word=False):
            if next is None:
                self.next = dict()
            elif isinstance(next, dict):
                self.next = next
            else:
                raise TypeError("Parameter 'next' nust be a dictionary.")
            self.word = bool(word)

    def __init__(self):
        self.__root = self.TrieNode()

    def insert(self, word: str) -> None:
        curNode = self.__root
        for char in word:
            if char not in curNode.next:
                curNode.next[char] = self.TrieNode()
            curNode = curNode.next[char]
        curNode.word = True

    def search(self, word: str) -> bool:
        _queue = deque()
        _queue.append((self.__root, 0))

        while _queue:
            curNode, i = _queue.popleft()

            if i == len(word):
                if curNode.word: return True
                continue

            if word[i].isalpha():
                if word[i] in curNode.next:
                    _queue.append((curNode.next[word[i]], i+1))
            else:
                for child in curNode.next.values():
                    _queue.append((child, i+1))
        return False

class WordDictionary:

    def __init__(self):
        self.__Trie = Trie()

    def addWord(self, word: str) -> None:
        self.__Trie.insert(word)

    def search(self, word: str) -> bool:
        return self.__Trie.search(word)


X = WordDictionary()
X.addWord("cat")
print(X.search("cat"))
print(X.search("c.t"))
print(X.search("..t."))
print(X.search("c."))

