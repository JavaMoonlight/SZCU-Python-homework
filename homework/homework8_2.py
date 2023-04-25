import re

abbreviation = input('Please enter a abbreviation: ')
sentence = input('Please enter a sentence: ')
list = ''
for i in range(0, len(abbreviation)):
    list += abbreviation[i]+"[a-z]+\s?([a-z]+ )?"
print(list)
result = re.search(list, sentence)
print(result.group())
