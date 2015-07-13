from random import shuffle

word = raw_input("Enter the word you want to scramble here: ")
word = list(word)
shuffle(word)
print ''.join(word)
