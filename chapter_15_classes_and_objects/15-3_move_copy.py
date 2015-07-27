# Exercise 15-3.
# Write a version of move_rectangle that creates and returns a new Rectangle instead of
# modifying the old one.

from point import Point
from rectangle import Rectangle

def move_rectangle(old_rec,dx,dy):
    """
    Takes a rectangle and distances, and returns a new Rectangle object
    moved by those coordinates.
    """
    new_rec = Rectangle()
    new_rec.height = old_rec.height
    new_rec.width = old_rec.width
    new_rec.corner = Point()
    new_rec.corner.x = old_rec.corner.x + dx
    new_rec.corner.y = old_rec.corner.y + dy
    return new_rec

original_rec = Rectangle()
original_rec.width = 10
original_rec.height = 10
original_rec.corner = Point()
original_rec.corner.x = 1
original_rec.corner.y = 2
dx = 1
dy = 1

new_rec = move_rectangle(original_rec,dx,dy)

print("New_rec is original_rec? %s" % (new_rec is original_rec))


