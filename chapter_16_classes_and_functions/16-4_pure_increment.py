# Exercise 16-4.
# Write a “pure” version of increment that creates and returns a new Time object rather
# than modifying the parameter.

from time_class import Time

def increment(time,seconds):
    t = Time()
    t.hour = time.hour + int(seconds/3600)
    t.minute = time.minute + int((seconds-int(seconds/3600))/60)
    t.second = time.second + (seconds % 60)
    return t

t = Time()
t.hour = 12
t.minute = t.second = 0
t2 = increment(t,3610)
print(t2.hour,t2.minute,t2.second,sep=":")
