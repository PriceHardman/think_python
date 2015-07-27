# Exercise 16-6.
# Write a function called mul_time that takes a Time object and a number and returns a
# new Time object that contains the product of the original Time and the number.
# Then use mul_time to write a function that takes a Time object that represents the
# finishing time in a race, and a number that represents the distance, and returns a Time
# object that represents the average pace (time per mile).

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

def mul_time(time,factor):
    return int_to_time(time_to_int(time)*factor)

def average_pace(finish,distance):
    return mul_time(finish,1/distance)

time = Time()
(time.hour,time.minute,time.second) = (1,10,5)
pace = average_pace(time,20)
print("Total Time: %.2d:%.2d:%.2d" % (time.hour,time.minute,time.second))
print("Total Distance: %dmi" % 20)
print("Pace per mile: %.2d:%.2d:%.2d" % (pace.hour,pace.minute,pace.second))
