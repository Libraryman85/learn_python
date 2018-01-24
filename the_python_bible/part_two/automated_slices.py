#can count from the end of a string, not just the beginning

word = 'supercalifragilisticexpialidocious'

print(word[-5])

print(word[-1])

print([word.index('cali')])

print(word[word.index('docious'):])
print(word[word.index('fragilistic'):word.index('exp')])

#.index only returns first instance of word/phrase you are searching for 