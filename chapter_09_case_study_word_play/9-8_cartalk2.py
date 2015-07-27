# Exercise 9-8.
# Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzler/transcripts/
# 200803):
# “I was driving on the highway the other day and I happened to notice my odometer. Like
# most odometers, it shows six digits, in whole miles only. So, if my car had 300,000 miles,
# for example, I’d see 3-0-0-0-0-0.
# “Now, what I saw that day was very interesting. I noticed that the last 4 digits were pal­
# indromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
# palindrome, so my odometer could have read 3-1-5-4-4-5.
# “One mile later, the last 5 numbers were palindromic. For example, it could have read
# 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
# you ready for this? One mile later, all 6 were palindromic!
# “The question is, what was on the odometer when I first looked?”
# Write a Python program that tests all the six-digit numbers and prints any numbers that
# satisfy these requirements.


def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


def are_adjacent_palindromes(number):
    """
    Returns True if both the last 4 digits of number and the last 5 digits of
    number+1 are palindromic. Else False.
    """
    if is_palindrome(str(number)[-4:]) and is_palindrome(str(number + 1)[-5:]):
        return True
    else:
        return False


i = 100000
while i <= 999999:
    if are_adjacent_palindromes(i):
        print(i, "and", i + 1)
    i += 1
