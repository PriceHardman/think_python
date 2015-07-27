# Exercise 10-1.
# Write a function called  nested_sum that takes a nested list of integers and add up the
# elements from all of the nested lists.


def nested_sum(nested_list):
    total = 0
    for list in nested_list:
        total += sum(list)
    return total

test_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
print(nested_sum(test_list))
