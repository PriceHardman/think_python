# Exercise 13-4.
# Modify the previous program to read a word list (see “Reading Word Lists” (page 97))
# and then print all the words in the book that are not in the word list. How many of them
# are typos? How many of them are common words that should be in the word list, and
# how many of them are really obscure?

import string


def word_frequency_in_file(filename):
    """
    Given txt file <filename>, return a dictionary of the words in the file
    and their frequencies.
    """
    words = {}
    fin = open(filename)
    punctuation = string.punctuation
    for line in fin:
        line = line.translate(  # Replace punctuation with spaces
            str.maketrans(punctuation, ' ' * len(punctuation)))
        line = line.lower()
        line_words = line.split()
        for word in line_words: # Process each word in the line.
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words

def book_words_not_in_word_file(book_file,word_file):
    book_words = word_frequency_in_file(book_file)
    words = word_frequency_in_file(word_file)
    words_not_in = {}
    for word in book_words:
        if word not in words:
            if word in words_not_in:
                words_not_in[word]+=1
            else:
                words_not_in[word]=1
    return words_not_in


words = []
books = ['hamlet','heart_of_darkness','ulysses']
for book in books:
    words += book_words_not_in_word_file(book+'.txt','words.txt')

for word in words:
    print(word)
