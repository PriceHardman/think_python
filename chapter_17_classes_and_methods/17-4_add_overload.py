# Exercise 17-4.
# Write an add method for the Point class.

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)

p1 = Point(3,4)
p2 = Point(6,3)
print(p1+p2)
