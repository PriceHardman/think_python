# Exercise 16-2.
# Write a boolean function called is_after that takes two Time objects, t1 and t2, and
# returns True if t1 follows t2 chronologically and False otherwise. Challenge: don’t use
# an if statement.

from time_class import Time

def is_after(t1,t2):
    """
    Returns True is t1 is later than t2 chronologically, else False.
    """
    t1_in_seconds = 60*(60*t1.hour + t1.minute) + t1.second
    t2_in_seconds = 60*(60*t2.hour + t2.minute) + t2.second
    times_in_seconds = {
        t1_in_seconds: True,
        t2_in_seconds: False
    }
    return times_in_seconds[max(t1_in_seconds,t2_in_seconds)]

t1 = Time()
t2 = Time()

t1.hour = t2.hour = 12
t1.minute = t2.minute = 10
t1.second = 1
t2.second = 2

print(is_after(t1,t2))
print(is_after(t2,t1))