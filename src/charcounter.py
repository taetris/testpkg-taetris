from collections import defaultdict
class CharCount:
    def __init__(self):
        pass

    @staticmethod
    def count(sentence):
        charDict = defaultdict(int)  # default val of int is 0
        for char in sentence:
                charDict[char]+=1
        return charDict


