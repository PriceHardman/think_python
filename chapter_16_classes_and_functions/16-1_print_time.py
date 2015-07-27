# Exercise 16-1.
# Write a function called print_time that takes a Time object and prints it in the form
# hour:minute:second. Hint: the format sequence '%.2d' prints an integer using at least
# two digits, including a leading zero if necessary.

from time_class import Time

def print_time(time):
    print("%.2d:%.2d:%.2d" % (time.hour,time.minute,time.second))

noon = Time()
noon.hour = 12
noon.minute = 0
noon.second = 0
print_time(noon)