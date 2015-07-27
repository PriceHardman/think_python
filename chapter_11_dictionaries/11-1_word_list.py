# Exercise 11-1.
# Write a function that reads the words in  words.txt and stores them as keys in a dic­
# tionary. It doesn’t matter what the values are. Then you can use the  in operator as a fast
# way to check whether a string is in the dictionary.
# If you did Exercise 10-11, you can compare the speed of this implementation with the
# list  in operator and the bisection search.

def create_dictionary(word_file):
    dictionary = {}
    fin = open(word_file)
    for line in fin:
        word = line.strip()
        dictionary[word]=None
    return dictionary

words = create_dictionary('words.txt')
print('found' in words)
