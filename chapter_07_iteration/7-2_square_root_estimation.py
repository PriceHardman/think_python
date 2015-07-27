# Exercise 7-2.
# Loops are often used in programs that compute numerical results by starting with an
# approximate answer and iteratively improving it.
# For example, one way of computing square roots is Newton’s method. Suppose that you
# want to know the square root of a. If you start with almost any estimate, x, you can
# compute a better estimate with the following formula:

#           y = (x+(a/x))/2

# When  y == x , we can stop. Here is a loop that starts with an initial estimate,  x , and
# improves it until it stops changing:

# while True:
#   print x
#   y = (x + a/x) / 2
#   if y == x:
#       break
#   x = y

# For most values of  a this works fine, but in general it is dangerous to test  float equality.
# Floating-point values are only approximately right: most rational numbers, like 1/3, and
# irrational numbers, like sqrt(2), can’t be represented exactly with a  float

# Rather than checking whether  x and  y are exactly equal, it is safer to use the built-in
# function  abs to compute the absolute value, or magnitude, of the difference between
# them:
# if abs(y-x) < epsilon:
# break
# Where  epsilon has a value like  0.0000001 that determines how close is close enough.

#   Write a function square_root that takes a as a parameter, chooses a reasonable value of x,
#   and returns an estimate of the square root of a.

def square_root(a):
    epsilon = 0.000001
    x = a/2
    while True:
        y = (x + a/x)/2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

# Test
a = float(input("Enter a number: "))
print("The square root of",a,"is approximately",square_root(a))
