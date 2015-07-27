# Exercise 7-1.
# Rewrite the function  print_n from “Recursion” (page 53) using iteration instead of
# recursion.

# Version using recursion:
def print_n_recur(s, n): # Print a string s n times.
    if n <= 0:
        return
    print(s)
    print_n_recur(s, n-1)

# Version using iteration:
def print_n_iter(s,n):
    if n <= 0:
        return
    while n > 0:
        print(s)
        n=n-1

# Test
s = input("Enter some text: ")
n = int(input("Enter a positive integer: "))
print("Using Recursion:")
print_n_recur(s,n)
print("Using iteration:")
print_n_iter(s,n)
