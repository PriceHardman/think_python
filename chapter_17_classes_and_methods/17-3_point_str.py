# Exercise 17-3.
# Write a str method for the Point class.
# Create a Point object and print it.

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)

p = Point(4,5)
print(p)
