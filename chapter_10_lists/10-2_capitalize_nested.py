# Exercise 10-2.
# Use  capitalize_all to write a function named  capitalize_nested that takes a nested
# list of strings and returns a new nested list with all strings capitalized.


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def capitalize_nested(nested_list):
    res = []
    for list in nested_list:
        res.append(capitalize_all(list))
    return res

test_list = [['a','b','c'],['d','e']]
print(capitalize_nested(test_list))
