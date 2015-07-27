# Exercise 17-2.
# Write an init method for the Point class that takes x and y as optional parameters and
# assigns them to the corresponding attributes.

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(1,2)
print("p = (%d,%d)" % (p.x,p.y))
