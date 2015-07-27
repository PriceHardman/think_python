# What does the following function do?
# def find(word, letter):
#   index = 0
#   while index < len(word):
#       if word[index] == letter:
#           return index
#       index = index + 1
#   return -1
# In a sense,  find is the opposite of the  [] operator. Instead of taking an index and ex­
# tracting the corresponding character, it takes a character and finds the index where that
# character appears. If the character is not found, the function returns  -1 .
# This is the first example we have seen of a  return statement inside a loop. If  word[index]
# == letter , the function breaks out of the loop and returns immediately.
# If the character doesn’t appear in the string, the program exits the loop normally and
# returns  -1 .
# This pattern of computation—traversing a sequence and returning when we find what
# we are looking for—is called a search.

# Exercise 8-4.
# Modify  find so that it has a third parameter, the index in  word where it should start
# looking.

def find(word, letter, start=0):
  index = start
  while index < len(word):
      if word[index] == letter:
          return index
      index = index + 1
  return -1

print(find("Python",'n',4))