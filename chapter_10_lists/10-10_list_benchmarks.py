# Exercise 10-10.
# Write a function that reads the file  words.txt and builds a list with one element per
# word. Write two versions of this function, one using the  append method and the other
# using the idiom  t = t + [x] . Which one takes longer to run? Why?
# Hint: use the  time module to measure elapsed time.

import time

def build_with_append():
    output = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        output.append(word)
    return output


def build_with_idiom():
    output = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        output = output + [word]
    return output

# Now run the benchmarks
append_start_time = time.time()
list1 = build_with_append()
append_end_time = time.time()

idiom_start_time = time.time()
list2 = build_with_idiom()
idiom_end_time = time.time()

print("Building using append took",append_end_time-append_start_time,"seconds.")
print("Building using idiom took",idiom_end_time-idiom_start_time,"seconds.")

# Append took 0.06 seconds,
# Idiomatic approach took 25 seconds (over 400x slower).
# My suspicion is that Python's lists are implemented as linked lists in C,
# and the append method simply adds another node onto the preexisting list,
# whereas the idiomatic method at each step creates an entirely new list
# and copies the old one to it. This is way more memory and operation-intensive.
