# Exercise 15-2.
# Write a function named move_rectangle that takes a Rectangle and two numbers
# named dx and dy. It should change the location of the rectangle by adding dx to the x
# coordinate of corner and adding dy to the y coordinate of corner.

from point import Point
from rectangle import Rectangle

def move_rectangle(rec,dx,dy):
    """Takes a rectangle object and moves it by dx and dy."""
    rec.corner.x += dx
    rec.corner.y += dy
    return None

rec = Rectangle()
rec.corner = Point()
rec.corner.x = 1
rec.corner.y = 2
rec.width = 10
rec.height = 15

dx = 2
dy = 3

print("Before: (x,y) = (%d,%d)" % (rec.corner.x,rec.corner.y))
move_rectangle(rec,dx,dy)
print("After: (x,y) = (%d,%d), (dx,dy) = (%d,%d)" % (rec.corner.x,rec.corner.y,dx,dy))