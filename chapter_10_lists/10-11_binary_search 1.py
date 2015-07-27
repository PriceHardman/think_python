# Exercise 10-11.
# To check whether a word is in the word list, you could use the  in operator, but it would
# be slow because it searches through the words in order.
# Because the words are in alphabetical order, we can speed things up with a bisection
# search (also known as binary search), which is similar to what you do when you look a
# word up in the dictionary. You start in the middle and check to see whether the word
# you are looking for comes before the word in the middle of the list. If so, then you search
# the first half of the list the same way. Otherwise you search the second half.
# Either way, you cut the remaining search space in half. If the word list has 113,809 words,
# it will take about 17 steps to find the word or conclude that it’s not there.
# Write a function called  bisect that takes a sorted list and a target value and returns the
# index of the value in the list, if it’s there, or  None if it’s not.

def bisect(sorted_list,value):
    lower = 0                         # index of lower bound of current interval
    upper = len(sorted_list)        # index of upper bound of current interval

    while lower <= upper:
        mid = int((lower+upper)/2)
        mid_value = sorted_list[mid]
        if value < mid_value:
            upper = mid-1
        elif value > mid_value:
            lower = mid+1
        else:
            return mid              # we've found it.
    return None                     # If we haven't found it, return None

import time

words = []
fin = open('words.txt')
for line in fin:
    words.append(line.strip())
words.sort()

# Compare performance of binary search and the 'in' idiom to find
# the word 'found'.

binary_start_time = time.time()
bisect(words,'find')!=None
binary_end_time = time.time()

in_start_time = time.time()
'find' in words
in_end_time = time.time()

print('Binary search took',binary_end_time-binary_start_time,'seconds.')
print('The \'in\' keyword took',in_end_time-in_start_time,'seconds.')
print(bisect(words,'find'))
print(words.index('find'))
