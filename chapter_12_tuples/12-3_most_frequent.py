# Exercise 12-3.
# Write a function called  most_frequent that takes a string and prints the letters in de­
# creasing order of frequency. Find text samples from several different languages and see
# how letter frequency varies between languages. Compare your results with the tables at
# http://en.wikipedia.org/wiki/Letter_frequencies.


def most_frequent(string):
    """Prints the letters of input string in decreasing order of frequency."""
    letters = {}
    for letter in list(string):
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    letters = sorted(
        [(freq, letter) for (letter, freq) in letters.items()],
        reverse=True)
    print([letter for freq, letter in letters])
