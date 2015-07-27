# Exercise 10-5.
# Write a function called  chop that takes a list, modifies it by removing the first and last
# elements, and returns  None

def chop(list):
    list.pop(0)
    list.pop(-1)
    return None


test_list = [1,2,3,4,5]
print('Before:',test_list)
chop(test_list)
print('After:',test_list)
