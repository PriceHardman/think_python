# Exercise 11-10.
# Two words are “rotate pairs” if you can rotate one
# of them and get the other (see rotate_word in Exercise 8-12).
# Write a program that reads a wordlist
# and finds all the rotate pairs.

def rotate_word(word, n):
    rotated_word = ''
    i = 0
    while i < len(word):
        rotated_word += chr(ord(word[i]) + n)
        i += 1
    return rotated_word

words = {}
fin = open('words.txt')
for line in fin:
    word = line.strip()
    words[word]=[] # initialize array for each word, will hold rotate pairs

n = len(words)
i=0

for word in words:
    for j in range(1,26):
        rotated_j = rotate_word(word,j)
        if rotated_j in words:
            words[word].append(rotated_j)
    i+=1
    if i%10000==0:
        print("Completed",i,"of",n)

for word in words:
    if len(words[word])>0:
        print(word,":",words[word])
