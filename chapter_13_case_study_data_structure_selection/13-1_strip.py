# Exercise 13-1.
# Write a program that reads a file, breaks each line into words, strips whitespace and
# punctuation from the words, and converts them to lowercase.
# Hint: The  string module provides strings named  whitespace , which contains space,
# tab, newline, etc., and  punctuation which contains the punctuation characters.
# Also, you might consider using the string methods  strip ,  replace and
# translate
import string


def strip_file(filename):
    words = []
    fin = open(filename)
    punctuation = string.punctuation
    for line in fin:
        line_words = line.translate(
            str.maketrans(punctuation, ' ' * len(punctuation)))
        line_words = line_words.lower()
        line_words = line_words.split()
        words += line_words
    return words

words = strip_file('hamlet.txt')

for i in words:
    print(i)
