# Exercise 12-6.
# Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzler/transcripts/
# 200651):
# What is the longest English word, that remains a valid English word, as you remove its
# letters one at a time?
# Now, letters can be removed from either end, or the middle, but you can’t rearrange any
# of the letters. Every time you drop a letter, you wind up with another English word. If you
# do that, you’re eventually going to wind up with one letter and that too is going to be an
# English word—one that’s found in the dictionary. I want to know what’s the longest word
# and how many letters does it have?
# I’m going to give you a little modest example: Sprite. Ok? You start off with sprite, you
# take a letter off, one from the interior of the word, take the r away, and we’re left with the
# word spite, then we take the e off the end, we’re left with spit, we take the s off, we’re left
# with pit, it, and I.
# Write a program to find all words that can be reduced in this way, and then find the
# longest one.
# This exercise is a little more challenging than most, so here are some suggestions:
# 1. You might want to write a function that takes a word and computes a list of all the
# words that can be formed by removing one letter. These are the “children” of the
# word.
# 2. Recursively, a word is reducible if any of its children are reducible. As a base case,
# you can consider the empty string reducible.
# 3. The wordlist I provided,  words.txt , doesn’t contain single letter words. So you
# might want to add “I”, “a”, and the empty string.
# 4. To improve the performance of your program, you might want to memoize the
# words that are known to be reducible.


def is_reducible(word):
    if len(word) == 0:  # base case '' is reducible
        return True
    if len(words[word]) == 0:  # words without children are not reducible
        return False
    for child in words[word]:
        if is_reducible(child):  # reducible if any children are
            return True
    else:
        return False  # not reducible if no children are


words = {}
reducible_words = []
fin = open('words.txt')
for line in fin:
    word = line.strip()
    words[word] = []
words['a'] = []
words['i'] = []
words[''] = []

# Compute all the children for each word,
# so that words[word] is a list of all the children of word.
for word in words:
    for i in range(0, len(word)):
        ith_removed = word[0:i] + word[i + 1:]
        if ith_removed in words:
            words[word].append(ith_removed)

n = len(words)
i = 0

for word in words:
    if is_reducible(word):
        reducible_words.append(word)
    i += 1
    if i % 10000 == 0:
        print(i, 'words processed of', n)

reducible_words.sort(key=len,reverse=True)
print("The longest reducible word is '",reducible_words[0],"'",sep='')

# => The longest reducible word is "complecting", with 11 letters.
