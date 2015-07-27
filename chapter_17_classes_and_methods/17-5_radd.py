# Exercise 17-5.
# Write an add method for Points that works with either a Point object or a tuple:
# - If the second operand is a Point, the method should return a new Point whose x
# coordinate is the sum of the x coordinates of the operands, and likewise for the y
# coordinates.
# - If the second operand is a tuple, the method should add the first element of the tuple
# to the x coordinate and the second element to the y coordinate, and return a new
# Point with the result.

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)

    def __add__(self,other):
        if isinstance(other,Point):
            return Point(self.x+other.x,self.y+other.y)
        elif isinstance(other,tuple):
            return Point(self.x+other[0],self.y+other[1])

    def __radd__(self,other):
        if isinstance(other,Point):
            return Point(self.x+other.x,self.y+other.y)
        elif isinstance(other,tuple):
            return Point(self.x+other[0],self.y+other[1])

p1 = Point(1,3)
p2 = Point(3,4)
p3 = (5,6)

print(p1+p2)
print(p3+p1)
