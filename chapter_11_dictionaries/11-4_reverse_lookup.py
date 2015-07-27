# Exercise 11-4.
# Modify  reverse_lookup so that it builds and returns a list of all keys that map to  v , or
# an empty list if there are none.

def reverse_lookup(dictionary,value):
    matching_keys = []
    for key in dictionary:
        if dictionary[key]==value:
            matching_keys.append(key)
    if len(matching_keys)==0:
        raise ValueError
    else:
        return matching_keys

