# Exercise 11-9.
# If you did Exercise 10-8, you already have a function named
# has_duplicates that takes a list as a parameter and returns
# True if there is any object that appears more than once in the list.
# Use a dictionary to write a faster, simpler version of  has_duplicates.

def has_duplicates(input_list):
    elements = {}
    for element in input_list:
        if element in elements:
            return True
        else:
            elements[element]=None
    return False

test_list = ['a','b','c','d','e','f','a','g','h'] # has two a's.
print(has_duplicates(test_list))
test_list = ['a','b','c','d','e','f','g','h'] # only unique values
print(has_duplicates(test_list))
