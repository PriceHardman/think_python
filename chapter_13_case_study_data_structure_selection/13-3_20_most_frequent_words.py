# Exercise 13-3.
# Modify the program from the previous exercise to print the 20 most frequently-used
# words in the book.

import string


def n_most_frequent_words_in_file(filename, n=20):
    """
    Given txt file <filename>, return the n most frequent words and
    and their frequencies, where n is defaulted to 20.
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
    words = words.items() # Convert from hash to list of tuples, for sorting.
    words = sorted(words, key=lambda words: words[1], reverse=True)
    return words[0:n]

conrad = n_most_frequent_words_in_file("heart_of_darkness.txt")
joyce = n_most_frequent_words_in_file('ulysses.txt')
print("Heart of Darkness,\tUlysses")
for i in range(0,20):
    print(conrad[i],joyce[i])
