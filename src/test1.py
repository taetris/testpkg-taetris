# Initial test file

from sample1 import TextTransform as sample

def sampleFunc():
    print(sample.lower("ALL SMALL"))
    print(sample.upper("all caps"))
    print(sample.title("the HUNGRY fox"))
    print(sample.kebab("hyphen text coming right up"))

sampleFunc()

