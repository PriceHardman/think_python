# Exercise 13-6.
# Python provides a data structure called  set that provides many common set operations.
# Read the documentation at http://docs.python.org/lib/types-set.html and write a program
# that uses set subtraction to find words in the book that are not in the
# word list.

import string


def words_in_text(filename):
    words = set()
    fin = open(filename)
    punctuation = string.punctuation
    punctuation += '‘’“”'
    for line in fin:
        for char in punctuation:
            if char == '-':
                line = line.replace(char, ' ')
            else:
                line = line.replace(char, '')
        line = line.lower()
        line_words = line.split()
        for word in line_words:
            if word not in words:
                try:                # ignore if the string is a number
                    float(word)
                    continue
                except ValueError:
                    words |= {word}
    return words

word_list = words_in_text('words.txt')  # List of every valid crossword entry.
hamlet = words_in_text('hamlet.txt')
conrad = words_in_text('heart_of_darkness.txt')
joyce = words_in_text('ulysses.txt')
grey = words_in_text('fifty_shades_of_grey.txt')

print("Work, Vocab Size, Non-Dictionary Words, Percent Non-Dictionary Words")
for title, file in [
    ("Hamlet's soliloquy", hamlet), ("Heart of Darkness", conrad),
        ("Ulysses", joyce), ("Fifty Shades of Grey", grey)]:
    total_words = len(file)
    invalids = len(file - word_list)
    percent_invalid = round((invalids / total_words) * 100)
    print("\t\t",title,", ",total_words,", ",invalids,", ",percent_invalid,"%",sep='')
