# Exercise 11-3.
# Dictionaries have a method called  keys that returns the keys of the dictionary, in no
# particular order, as a list.
# Modify  print_hist to print the keys and their values in alphabetical order.

def print_hist(hist):
    keys = list(hist.keys())    # Book assumes Python 2.x.
    keys.sort()
    for key in keys:
        print(key,': ',hist[key],sep='')

test_hist = {'e':1,'d':2,'c':3,'b':4,'a':5}
print_hist(test_hist)
