# Exercise 12-1.
# Many of the built-in functions use variable-length argument tuples. For example,  max
# and  min can take any number of arguments:
# >>> max(1,2,3)
# 3
# But sum does not.
# >>> sum(1,2,3)
# TypeError: sum expected at most 2 arguments, got 3
# Write a function called  sumall that takes any number of arguments and returns their
# sum.

def sumall(*args):
    output=0
    for i in args:
        output+=i
    return output

print(sumall(1,2,3,4,5,6,7)) # => (7*8/2)=28
