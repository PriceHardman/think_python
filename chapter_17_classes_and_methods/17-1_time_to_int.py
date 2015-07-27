# Exercise 17-1.
# Rewrite time_to_int (from “Prototyping Versus Planning” (page 184)) as a method. It
# is probably not appropriate to rewrite int_to_time as a method; what object you would
# invoke it on?

class Time(object):
    """A simple class for time."""
    def time_to_int(self):
        return self.hour*3600 + self.minute * 60 + self.second

t = Time()
t.hour = 2
t.minute = 10
t.second = 4
print(t.time_to_int())
