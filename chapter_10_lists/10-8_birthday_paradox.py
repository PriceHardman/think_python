# Exercise 10-8.
# The (so-called) Birthday Paradox:
# 1. Write a function called  has_duplicates that takes a list and returns  True if there
# is any element that appears more than once. It should not modify the
# original list.

def has_duplicates(list):
    list2 = list[:]
    list2.sort()

    if len(list2) == 0:
        return False

    previous_element = list2[0]
    i = 1
    while i < len(list2):
        if list2[i] == previous_element:
            return True
        previous_element = list2[i]
        i += 1
    return False

# 2. If there are 23 students in your class, what are the chances that two of you have the
# same birthday? You can estimate this probability by generating random samples of
# 23 birthdays and checking for matches. Hint: you can generate random birthdays
# with the  randint function in the  random module.
# You can read about this problem at
# http://en.wikipedia.org/wiki/Birthday_paradox

import random

count_with_same_birthday = 0
count_without_same_birthday = 0

i = 0
number_of_trials = 10000
while i <= number_of_trials:
    # Create a 23-element list of random ints between 1 and 365.
    class_birthdays = [random.randint(1,365) for x in range(0,23)]

    if has_duplicates(class_birthdays):
        count_with_same_birthday+=1
    else:
        count_without_same_birthday+=1
    i+=1

print("Probability of same birthday:",count_with_same_birthday/number_of_trials)

# For n=23 people, the probability appears around 50%.
