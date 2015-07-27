# Exercise 6-6.
# A palindrome is a word that is spelled the same backward and forward, like “noon” and
# “redivider.” Recursively, a word is a palindrome if the first and last letters are the same
# and the middle is a palindrome.
# The following are functions that take a string argument and return the first, last, and
# middle letters:
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# We’ll see how they work in Chapter 8.
#   1. Type these functions into a file named  palindrome.py and test them out. What
#   happens if you call  middle with a string with two letters? One letter? What about
#   the empty string, which is written  '' and contains no letters?

print("middle(\"ab\")=\"",middle("ab"),"\"",sep="")
print("middle(\'\')=\"",middle(''),"\"",sep="")


#   2. Write a function called  is_palindrome that takes a string argument and returns
#   True if it is a palindrome and  False otherwise. Remember that you can use the
#   built-in function  len to check the length of a string.
#   Solution: http://thinkpython.com/code/palindrome_soln.py.

def is_palindrome(input):
    #   if len==0 return False
    #   elif first==last,
    #       if len==2 or len==1 return TRUE,
    #       else return is_palindrome(middle)
    #   else return FALSE
    if len(input)==0:
        return False
    elif first(input)==last(input):
        if len(input)==1 or len(input)==2:
            return True
        else:
            return is_palindrome(middle(input))
    else:
        return False

print(is_palindrome("radar"))


# Much simpler function,
# but making use of features not
# yet seen in the text.
def is_palindrome2(input):
    if input==input[::-1]:
        return True
    else:
        return False

print(is_palindrome2("radar"))