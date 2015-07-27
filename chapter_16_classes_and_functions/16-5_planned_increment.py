# Exercise 16-5.
# Rewrite increment using time_to_int and int_to_time.

from time_class import Time

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def increment(time,seconds):
    return int_to_time(time_to_int(time)+seconds)

t = Time()
t.hour = 12
t.minute = t.second = 0
t2 = increment(t,3610)
print(t2.hour,t2.minute,t2.second,sep=":")
