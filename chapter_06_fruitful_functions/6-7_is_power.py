# Exercise 6-7.
# A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function
# called  is_power that takes parameters  a and  b and returns  True if  a is a power of  b . Note:
# you will have to think about the base case.

def is_power(a,b):
    # The logic is as follows:
    #   If the
    if a==b:
        return True
    elif a%b == 0:
        return is_power(a/b,b)
    else:
        return False


# Test
a = int(input("Enter an integer:"))
b = int(input("Enter another integer:"))
print(a,"is a power of",b,":",is_power(a,b))