# Exercise 14-1.
# The os module provides a function called walk that is similar to this one
# but more versatile.

# def walk(dirname):
#     for name in os.listdir(dirname):
#     path = os.path.join(dirname, name)
#     if os.path.isfile(path):
#     print path
#     else:
#     walk(path)
# os.path.join takes a directory and a file name
# and joins them into a complete path.

# Read the documentation and use it to print the
# names of the files in a given directory and its subdirectories.

import os
for filename in os.walk("../"):
    print(filename)
