# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store
# and retrieve keys in a dataset of strings. There are various applications of this data structure,
# such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix,
# and false otherwise.

class Trie1:

    def __init__(self):
        self._trie_dict = [False, dict()]

    def insert(self, word: str) -> None:
        curNode = self._trie_dict
        i = 0
        while i < len(word):
            if word[i] not in curNode[1]:
                curNode[1][word[i]] = [bool(i == (len(word)-1)), dict()]
            curNode = curNode[1][word[i]]
            i += 1
        else:
            if i >= len(word): curNode[0] = True

    def search(self, word: str) -> bool:
        curNode = self._trie_dict
        i = 0
        while i < len(word):
            if word[i] not in curNode[1]:
                return False
            curNode = curNode[1][word[i]]
            i += 1
        else:
            if i >= len(word):
                return curNode[0]


    def startsWith(self, prefix: str) -> bool:
        curNode = self._trie_dict
        i = 0
        while i < len(prefix):
            if prefix[i] not in curNode[1]:
                return False
            curNode = curNode[1][prefix[i]]
            i += 1
        else:
            if i >= len(prefix): return True


class Trie:

    class TrieNode:
        """
        Represents a node in a Trie data structure.

        Attributes:
            next (dict): A dictionary mapping characters to TrieNode objects.
            word (bool): Indicates if the node represents the end of the word.
        """
        def __init__(self, next=None, word=False):
            if next is None:
                self.next = dict()
            elif isinstance(next, dict):
                self.next = next
            else:
                raise ValueError("Parameter 'next' nust be a dictionary.")
            self.word = bool(word)

    def __init__(self):
        self.rootNode = self.TrieNode()

    def insert(self, word: str) -> None:
        curNode = self.rootNode
        for char in word:
            if char not in curNode.next:
                curNode.next[char] = self.TrieNode()
            curNode = curNode.next[char]
        curNode.word = True

    def search(self, word: str) -> bool:
        curNode = self.rootNode
        for char in word:
            if char not in curNode.next:
                return False
            curNode = curNode.next[char]
        return curNode.word

    def startsWith(self, prefix: str) -> bool:
        curNode = self.rootNode
        for char in prefix:
            if char not in curNode.next:
                return False
            curNode = curNode.next[char]
        return True


X = Trie()
X.insert("apple")
X.insert("app")
print(X.search("apple"))
print(X.search("app"))


