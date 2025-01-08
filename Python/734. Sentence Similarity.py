# We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be
# represented as arr = ["I","am",happy","with","leetcode"].
#
# Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs
# similarPairs where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.
#
# Return true if sentence1 and sentence2 are similar, or false if they are not similar.
#
# Two sentences are similar if:
#
# They have the same length (i.e., the same number of words)
# sentence1[i] and sentence2[i] are similar.
# Notice that a word is always similar to itself, also notice that the similarity relation is not transitive.
# For example, if the words a and b are similar, and the words b and c are similar, a and c are not necessarily similar.
from typing import List
from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if (our_len:=len(sentence1)) != len(sentence2):
            return False

        our_dict = defaultdict(set)
        for pair in similarPairs:
            our_dict[pair[0]].add(pair[1])
            our_dict[pair[1]].add(pair[0])

        for i in range(our_len):
            if sentence1[i] != sentence2[i]:
                if not sentence1[i] in our_dict or not sentence2[i] in our_dict[sentence1[i]]:
                    return False
        return True


sentence1 = ["one","excellent","meal"]
sentence2 = ["one","good","dinner"]
similarPairs = [
    ["great","good"],
    ["extraordinary","good"],
    ["well","good"],
    ["wonderful","good"],
    ["excellent","good"],
    ["fine","good"],
    ["nice","good"],
    ["any","one"],
    ["some","one"],
    ["unique","one"],
    ["the","one"],
    ["an","one"],
    ["single","one"],
    ["a","one"],
    ["truck","car"],
    ["wagon","car"],
    ["automobile","car"],
    ["auto","car"],
    ["vehicle","car"],
    ["entertain","have"],
    ["drink","have"],
    ["eat","have"],
    ["take","have"],
    ["fruits","meal"],
    ["brunch","meal"],
    ["breakfast","meal"],
    ["food","meal"],
    ["dinner","meal"],
    ["super","meal"],
    ["lunch","meal"],
    ["possess","own"],
    ["keep","own"],
    ["have","own"],
    ["extremely","very"],
    ["actually","very"],
    ["really","very"],
    ["super","very"]
]
x = Solution()
print(x.areSentencesSimilar(sentence1, sentence2, similarPairs))