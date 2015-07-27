# Exercise 10-6.
# Write a function called  is_sorted that takes a list as a parameter and returns  True if
# the list is sorted in ascending order and  False otherwise. You can assume (as a precon­
# dition) that the elements of the list can be compared with the relational operators  < ,  > ,
# etc.
# For example,  is_sorted([1,2,2]) should return  True and  is_sorted(['b','a'])
# should return  False


def is_sorted(input_list):
    sorted_list = input_list[:]
    sorted_list.sort()
    i = 0
    while i < len(input_list):
        if input_list[i] != sorted_list[i]:
            return False
        i += 1
    return True
