# Exercise 9-5.
# Write a function named  uses_all that takes a word and a string of required letters, and
# that returns  True if the word uses all the required letters at least once. How many words
# are there that use all the vowels  aeiou ? How about  aeiouy?

def uses_all(word,letters):
    for letter in letters: # loop through the needed letters
        if letter not in word: # check for the given letter in the word
            return False # return False if its not there
    return True # if we get here, all letters are there, so return True

uses_aeiou = 0
uses_aeiouy = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if uses_all(word,'aeiouy'):
        uses_aeiouy += 1
    elif uses_all(word,'aeiou'):
        uses_aeiou += 1
    else:
        None

print("Words that use 'aeiou':",uses_aeiou)
print("words that use 'aeiouy':",uses_aeiouy)


