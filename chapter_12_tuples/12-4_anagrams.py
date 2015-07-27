# Exercise 12-4.
# More anagrams!

# 1. Write a program that reads a word list from a file (see “Reading Word Lists” (page
# 97)) and prints all the sets of words that are anagrams.
# Here is an example of what the output might look like:
# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
# ['retainers', 'ternaries']
# ['generating', 'greatening']
# ['resmelts', 'smelters', 'termless']
# Hint: you might want to build a dictionary that maps from a set of letters to a list
# of words that can be spelled with those letters. The question is, how can you rep­
# resent the set of letters in a way that can be used as a key?


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

anagrams = get_anagrams('words.txt')

# 2. Modify the previous program so that it prints the largest set of anagrams first,
# followed by the second largest set, and so on.
sorted_anagrams = sorted(
    [val for (key, val) in anagrams.items()], key=len, reverse=True)

print(anagrams.items())
# Uncomment the next three lines to print out all anagrams in desc order (~15 sec)
# for anagram_set in sorted_anagrams:
#     if len(anagram_set) > 1:
#         print(len(anagram_set),anagram_set)

# 3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter
# on the board, to form an eight-letter word. What set of 8 letters forms the most
# possible bingos? Hint: there are seven.

# eight_letter_sets = sorted(
#     [val for (key, val) in anagrams.items() if len(key) == 8],
#         key=len, reverse=True)

# print("Letters with most bingos:",tuple(sorted(eight_letter_sets[0][0])))
# print("Words formed by that set:",eight_letter_sets[0])
