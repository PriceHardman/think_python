# Exercise 8-1.
# Write a function that takes a string as an argument and displays the letters backward,
# one per line.

def reverse(string):
    i = 0
    n = len(string)-1
    while i <= n:
        print(string[n-i])
        i+=1

reverse("hello")