# Exercise 16-7.
# The datetime module provides date and time objects that are similar to the Date and
# Time objects in this chapter, but they provide a rich set of methods and operators. Read
# the documentation at http://docs.python.org/lib/datetime-date.html.

from datetime import date as date
from datetime import datetime as datetime


# 1. Use the datetime module to write a program that gets the current date and prints
# the day of the week.
days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}
today = days[datetime.today().weekday()]
print("Today is %s" % today)

# 2. Write a program that takes a birthday as input and prints the user’s age and the
# number of days, hours, minutes and seconds until their next birthday.
# birthday_string = input("Enter your birthday in the form 'mm/dd/yyyy': ")
# birthday = datetime.strptime(birthday_string,"%m/%d/%Y")
# today = datetime.today()
# age = int((today-birthday).days / 365)
# this_years_birthday = birthday.replace(year=today.year)
# next_years_birthday = birthday.replace(year=today.year+1)
# if (today < this_years_birthday):
#     next_birthday = this_years_birthday
# else:
#     next_birthday = next_years_birthday
# print(
#     "Birthdate: %.2d/%.2d/%.4d, Current age: %d, Next Birthday: %.2d/%.2d/%.4d" %
#     (birthday.month,birthday.day,birthday.year,age,next_birthday.month,next_birthday.day,next_birthday.year)
# )


# 3. For two people born on different days, there is a day when one is twice as old as the
# other. That’s their Double Day. Write a program that takes two birthdays and com-
# putes their Double Day.

def double_day(b1,b2):
    """
        Takes two birthdays as date objects
        and returns a date for their Double Day.
    """
    # Given birthdays b1 and b2, we seek a d such that (d-b1) = 2*(d-b2) => d = 2*b2 - b1
    # To make sure we don't get a nonsensical answer where d is negative,
    # if 2*b2 - b1 < 0 , return 2*b1 - b2 instead.
    today = date.today()
    b1_age = (today-b1)
    b2_age = (today-b2)
    if b2 > b1:
        d = today - (2*b2_age - b1_age)
    else:
        d = today - (2*b1_age - b2_age)
    return d


b1 = date(1951,7,14)
b2 = date(1989,9,5)
print("Double day for %s and %s: %s" %(b1,b2,double_day(b1,b2)))

# 4. For a little more challenge, write the more general version that computes the day
# when one person is n times older than the other.
def n_day(b1,b2,n):
    """
        Takes two birthdays as date objects
        and integer n and returns a date for their n-day.
    """
    # Given birthdays b1 and b2, we seek a d such that (d-b1) = n*(d-b2) => d = n*b2 - b1
    # To make sure we don't get a nonsensical answer where d is negative,
    # if n*b2 - b1 < 0 , return n*b1 - b2 instead.
    today = date.today()
    b1_age = (today-b1)
    b2_age = (today-b2)
    if b2 > b1:
        d = today - (n*b2_age - b1_age)
    else:
        d = today - (n*b1_age - b2_age)
    return d

b1 = date(1949,8,8)
b2 = date(1989,9,5)
print("n=3 day for %s and %s: %s" %(b1,b2,n_day(b1,b2,3)))
