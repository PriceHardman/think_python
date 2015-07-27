# Exercise 10-4.
# Write a function called  middle that takes a list and returns a new list that contains all
# but the first and last elements. So  middle([1,2,3,4]) should return  [2,3]


def middle(list):
    output = list
    output.pop(0)
    output.pop(-1)
    return output

print(middle([1, 2, 3, 4, 5]))
