# For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence.
# The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence.
# If word is not a substring of sequence, word's maximum k-repeating value is 0.
#
# Given strings sequence and word, return the maximum k-repeating value of word in sequence.

def maxRepeating1(sequence: str, word: str) -> int: # не правильно, не соответствует условию задачи
    # start from prefix function
    OurPrefFun = [0] * len(word)
    i, j = 1, 0
    while i < len(word):
        if word[i] == word[j]:
            OurPrefFun[i] = j + 1
            i += 1; j += 1
        else:
            if j == 0:
                OurPrefFun[i] = 0
                i += 1
            else:
                j = OurPrefFun[j-1]

    # find all substrings
    OurCountStr = 0
    i = j = 0
    while i < len(sequence):
        if sequence[i] == word[j]:
            if j == (len(word)-1):
                j = 0; i = i - len(word) + 2; OurCountStr += 1
            else:
                i += 1; j += 1
        else:
            if j > 0:
                j = OurPrefFun[j-1]
            else:
                i += 1
    return OurCountStr



def maxRepeating2(sequence: str, word: str) -> int:
    i = j = CurrentCount = ResultCount = 0
    while i < len(sequence):
        if sequence[i] == word[j]:
            if j == (len(word)-1):
                i += 1; j = 0; CurrentCount += 1
            else:
                i += 1; j += 1
        else:
            i = (i - j + 1 if CurrentCount == 0 else i - (CurrentCount*(len(word)-1)))
            j = 0
            ResultCount = max(ResultCount, CurrentCount)
            CurrentCount = 0
    else:
        ResultCount = max(ResultCount, CurrentCount)
    return ResultCount

sequence = "abacaa"; word = "a"
print(maxRepeating2(sequence, word))