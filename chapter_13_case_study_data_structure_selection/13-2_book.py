# Exercise 13-2.
# Go to Project Gutenberg (http://www.gutenberg.org) and download your favorite out-
# of-copyright book in plain text format.
# Modify your program from the previous exercise to read the book you downloaded,
# skip over the header information at the beginning of the file, and process the rest of the
# words as before.
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

conrad = strip_file('heart_of_darkness.txt')
joyce = strip_file('ulysses.txt')

# Then modify the program to count the total number of words in the book, and the
# number of times each word is used.

conrad_word_freq = {}
for word in conrad:
    if word in conrad_word_freq:
        conrad_word_freq[word] += 1
    else:
        conrad_word_freq[word] = 0

joyce_word_freq = {}
for word in joyce:
    if word in joyce_word_freq:
        joyce_word_freq[word] += 1
    else:
        joyce_word_freq[word] = 0


# Print the number of different words used in the book. Compare different books by
# different authors, written in different eras. Which author uses the most extensive
# vocabulary?

print("Number of distinct words used in Heart of Darkness:", len(conrad_word_freq))
print("Number of distinct words used in Ulysses:", len(joyce_word_freq))
