class CharCount:
    def __init__(self):
        pass

    @staticmethod
    def count(sentence):
        charDict = {}   
        for char in sentence:
            if (char.lower() not in charDict):
                charDict.update({char.lower() : 1})
            else:
                charDict[char]+=1
        return charDict


