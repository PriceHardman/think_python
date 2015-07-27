# Exercise 15-1.
# Write a function called distance_between_points that takes two Points as arguments
# and returns the distance between them.

import math
from point import Point

def distance_between_points(p1,p2):
    return math.sqrt((p2.y-p1.y)**2 + (p2.x-p1.x)**2)

p1 = Point()
p2 = Point()

p1.x = -1
p1.y = -2
p2.x = 3
p2.y = 4

print(distance_between_points(p1,p2))