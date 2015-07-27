# Exercise 12-2.
# In this example, ties are broken by comparing words, so words with the same length
# appear in reverse alphabetical order. For other applications you might want to break ties
# at random. Modify this example so that words with the same length appear in random
# order. Hint: see the  random function in the  random module.

# Example to modify:


def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res

import random


def sort_by_length2(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))
    t.sort(reverse=True)
    res = []
    for length, rand, word in t:
        res.append(word)
    return res

test = ['a','b','c','d','aa','bb','cc','dd','aaa']
print(sort_by_length(test)) # sorted by length desc, alphabetical desc
print(sort_by_length2(test)) # sorted by length desc, random
