# Exercise 11-5.
# Read the documentation of the dictionary method  setdefault and use it to write a
# more concise version of  invert_dict . Solution: http://thinkpython.com/code/
# invert_dict.py.

def invert_dict(dictionary):
    inverse = {}
    for key in dictionary:
        value = dictionary[key]
        inverse.setdefault(value,[]).append(key)
    return inverse

x = {'a':1,'b':2,'c':1,'d':3,'e':1}
print(invert_dict(x))

