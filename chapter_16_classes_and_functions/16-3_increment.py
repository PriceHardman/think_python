# Exercise 16-3.
# Write a correct version of increment that doesn’t contain any loops.
# That is, write a function that takes two arguments, a time object, and an integer representing a number of seconds,
# and modify the original time object by adding that number of seconds to it.

from time_class import Time

def increment(time,seconds):
    hours_to_add = int(seconds/3600)
    minutes_to_add = int((seconds-3600*hours_to_add)/60)
    seconds_to_add = int(seconds % 60)
    time.hour += hours_to_add
    time.minute += minutes_to_add
    time.second += seconds_to_add

t = Time()
t.hour = t.minute = t.second = 0
increment(t,3700)
print("Time = %.2d:%.2d:%.2d" % (t.hour,t.minute,t.second))