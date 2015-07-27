# Exercise 14-3.
# If you download my solution to Exercise 12-4 from
# http://thinkpython.com/code/anagram_sets.py, you’ll see that it creates a
# dictionary that maps from a sorted string of letters to the list of words that
# can be spelled with those letters. For example, ’opst’ maps to the list [’opts’,
# ’post’, ’pots’, ’spot’, ’stop’, ’tops’]. Write a module that imports
# anagram_sets and provides two new functions: store_anagrams should store the
# anagram dictionary in a “shelf;” read_anagrams should look up a word and return
# a list of its anagrams.

import pickle


def get_anagrams(word_file, count=False):
    counter = 0
    anagrams = {}
    fin = open(word_file)
    for line in fin:
        word = line.strip()
        letters = list(word)
        letters.sort()
        letters = tuple(letters)

        if letters in anagrams:
            anagrams[letters].append(word)
        else:
            anagrams[letters] = [word]

        if count == True and counter % 1000 == 0:
            print(counter)
        counter += 1
    return anagrams

def store_anagrams(anagrams):
    return pickle.dumps(anagrams)

def read_anagrams(shelf,word):
    letters_in_word = tuple(sorted(list(word.lower())))
    return pickle.loads(shelf)[letters_in_word]

shelf = store_anagrams(get_anagrams('words.txt'))
print(read_anagrams(shelf,"Python"))