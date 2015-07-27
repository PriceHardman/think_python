# Exercise 13-7.
# To choose a random word from the histogram, the simplest algorithm is to build a list
# with multiple copies of each word, according to the observed frequency, and then choose
# from the list:

# def random_word(h):
#     t = []
#     for word, freq in h.items():
#         t.extend([word] * freq)
#     return random.choice(t)

# The expression  [word] * freq creates a list with  freq copies of the string  word . The
# extend method is similar to  append except that the argument is a sequence.
# This algorithm works, but it is not very efficient; each time you choose a random word,
# it rebuilds the list, which is as big as the original book. An obvious improvement is to
# build the list once and then make multiple selections, but the list is still big.

# An alternative is:
# 1. Use  keys to get a list of the words in the book.
# 2. Build a list that contains the cumulative sum of the word frequencies (see
# Exercise 10-3). The last item in this list is the total number of words in the book, n.
# 3. Choose a random number from 1 to n. Use a bisection search (See Exercise 10-11)
# to find the index where the random number would be inserted in the cumulative
# sum.
# 4. Use the index to find the corresponding word in the word list.

# Write a program that uses this algorithm to choose a random word from the book.

import random
import string

def histogram(elements):
    hist = {}
    for x in elements:
        if x in hist:
            hist[x] += 1
        else:
            hist[x] = 1
    return hist

def random_word(h):
    """A more efficient method for returning a random element from a histogram"""
    words = h.keys()
    cumulative_sum = []
    for word in words:
        cumulative_sum.append(h[word])

    n = cumulative_sum[-1]
    r = random.randint(0,n)



test = ['a','b','a','a','c','d','e','e']

hist = histogram(test)
rword = random_word(hist)

print(hist)
print(rword)
