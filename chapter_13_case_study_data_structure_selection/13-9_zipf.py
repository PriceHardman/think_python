# Exercise 13-9.
# The “rank” of a word is its position in a list of words sorted by frequency:
# the most common word has rank 1, the second most common has rank 2, etc.
# Zipf ’s law describes a relationship between the ranks and frequencies of
# words in natural languages (http://en.wikipedia.org/wiki/Zipfs_law).
# Specifically, it predicts that the frequency, f, of the word with rank r is:
#                           f = cr^(-s)
# where s and c are parameters that depend on the language and the text.
# If you take the logarithm of both sides of this equation, you get:
#                      log f = log c - s log r
# So if you plot log f versus log r, you should get a straight line
# with slope -s and intercept log c.
# Write a program that reads a text from a file, counts word frequencies,
# and prints one line for each word, in descending order of frequency,
# with log f and log r. Use the graphing program of your choice to
# plot the results and check whether they form a straight line.
# Can you estimate the value of s?

import string
from math import log as log
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def frequency(text):
    """Returns a dictionary of the ranks and frequencies of words in text."""

    words = {}
    punctuation = string.punctuation
    fin = open(text)
    for line in fin:
        line = line.translate(str.maketrans(punctuation, ' ' * len(punctuation)))
        line = line.lower()
        line_words = line.split()
        for word in line_words:
            if word in words:
                words[word]['freq'] += 1
            else:
                words[word] = {'freq': 1, 'rank': 0}
    words = sorted(
        [[key,val['freq'],val['rank']] for key,val in words.items()],
        key = lambda x: x[1],
        reverse = True
    )
    for i,element in enumerate(words):
        words[i][2] = i+1
    return [(x[0],log(x[1]),log(x[2])) for x in words]

data = frequency('heart_of_darkness.txt')

for word in data:
    print("Word:'",word[0],
          "'\tlog f: ",round(word[1],2),
          "\tlog r: ",round(word[2],2),sep="")



# Plot log(f) vs log(r) for Heart of Darkness
pd.options.display.mpl_style = 'default' # make the chart look nice.
df = pd.DataFrame([[word[1],word[2]] for word in data],columns=["log f","log r"])
df.plot(x='log f',y='log r').get_figure().savefig("zipf.pdf")

# Estimate c and s
x = np.array(df['log r'])
y = np.array(df['log f'])
X = np.vstack([x,np.ones(len(x))]).T
s,c = np.linalg.lstsq(X,y)[0]
print("Estimates: s_hat =",round(s,2),"c_hat=",round(c,2))
