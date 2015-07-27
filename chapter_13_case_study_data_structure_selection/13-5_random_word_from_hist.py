# Exercise 13-5.
# Write a function named  choose_from_hist that takes a histogram as defined in “Dic­
# tionary as a Set of Counters” (page 123) and returns a random value from the histogram,
# chosen with probability in proportion to frequency. For example, for this histogram:
# >>> t = ['a', 'a', 'b']
# >>> hist = histogram(t)
# >>> print hist
# {'a': 2, 'b': 1}
# your function should return  ’a’ with probability 2/3 and  ’b’ with
# probability 1/3.
import random


def histogram(elements):
    hist = {}
    for x in elements:
        if x in hist:
            hist[x] += 1
        else:
            hist[x] = 1
    return hist

# This exercise is somewhat silly, because to get a list of values
# from which elements can be chosen with probability in proportion to
# their frequency in the histogram, we simply need to recreate
# the original population from which the histogram was created in the
# first place.
# For example, given original list ['a','a','b'], we get histogram
# {'a':2, 'b':1}. To obtain a sample where P(a)=2/3 and P(b)=1/3, all
# we need to do is perform random.sample(['a','a','b']). Thus, we
# just need to recover the original population from the histogram.


def choose_from_hist(hist):
    """
    Given a histogram, return a random value chosen with probability
    in proportion to the frequency.
    """
    population = []
    for key in hist:
        for i in range(0, hist[key]):
            population.append(key)
    return random.choice(population)

test = ['a', 'a', 'b', 'c', 'c', 'c', 'd', 'd']

# Perform a Monte Carlo simulation to confirm our method is sound:
n = 100000
hist = histogram(test)
results = {}
for i in range(0, n):
    choice = choose_from_hist(hist)
    if choice in results:
        results[choice] += 1
    else:
        results[choice] = 1

for key in results:
    print(key, "was chosen with probability of", round(results[key] / n, 2))

# Results should be:
# a~=2/8=1/4=0.25
# b~=1/8=0.125
# c~=3/8=(0.25+0.125)=0.375
# d~=2/8=1/4=0.25
