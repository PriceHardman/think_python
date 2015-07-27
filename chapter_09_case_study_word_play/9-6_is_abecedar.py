# Exercise 9-6.
# Write a function called  is_abecedarian that returns  True if the letters in a word appear
# in alphabetical order (double letters are ok). How many abecedarian words are there?

def is_abecedarian(word):
    previous_letter = word[0]
    for current_letter in word:
        if current_letter < previous_letter:
            return False
        previous_letter = current_letter
    return True



