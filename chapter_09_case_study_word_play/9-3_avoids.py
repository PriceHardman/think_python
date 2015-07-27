# Exercise 9-3.
# Write a function named  avoids that takes a word and a string of forbidden letters, and
# that returns  True if the word doesn’t use any of the forbidden letters.
# Modify your program to prompt the user to enter a string of forbidden letters and then
# print the number of words that don’t contain any of them. Can you find a combination
# of 5 forbidden letters that excludes the smallest number of words?

def avoids(word,forbidden_letters):
    for forbidden_letter in forbidden_letters:
        if forbidden_letter in word:
            return False
    return True # Only returns True if it doesn't see any of the letters.


# Prompt the user for a string of forbidden letters.
forbidden_letters = input("Enter a string of forbidden letters: ")

number_of_words_that_avoid = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    number_of_words_that_avoid+=1 if avoids(word,forbidden_letters) else 0

print(number_of_words_that_avoid)

