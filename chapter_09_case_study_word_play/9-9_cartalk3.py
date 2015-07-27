# Exercise 9-9.
# Here’s another Car Talk Puzzler you can solve with a search (http://www.cartalk.com/
# content/puzzler/transcripts/200813):
# “Recently I had a visit with my mom and we realized that the two digits that make up my
# age when reversed resulted in her age. For example, if she’s 73, I’m 37. We wondered how
# often this has happened over the years but we got sidetracked with other topics and we
# never came up with an answer.
# “When I got home I figured out that the digits of our ages have been reversible six times
# so far. I also figured out that if we’re lucky it would happen again in a few years, and if
# we’re really lucky it would happen one more time after that. In other words, it would have
# happened 8 times over all. So the question is, how old am I now?”
# Write a Python program that searches for solutions to this Puzzler. Hint: you might find
# the string method  zfill useful.

# Loop through a range of appropriate age gaps (15 to 50),
# and for each gap, loop through a range of appropriate ages for the son (0 to 100).
# Based on the son's age, create a reciprocal mom_age (adding a leading 0 to the
# son's age if the son's age is single-digit.). If mom_age-son_age equals the given
# age gap, we have a candidate. Print each candidate pair of ages, keeping track
# of how many have been found for each age gap. We're looking for the son's age
# at the sixth candidate pair on an age gap that yields 8 such pairs.

age_gap = 15
while age_gap < 50:
    i = 0
    print("Age gap:", age_gap)
    son_age = 0
    while son_age < 100:
        if len(str(son_age))==1:
            mom_age = int(str(son_age).zfill(2)[::-1])
        else:
            mom_age = int(str(son_age)[::-1])
        if mom_age-son_age == age_gap:
            i+=1
            print("\t",i,": ",son_age," and ",mom_age,sep='')
        son_age+=1
    age_gap+=1

# The only age gap that yielded 8 valid reciprocal ages was 18 years,
# in which the son's age during the 6th cooincidence was 57.

# ANSWER: He is currently 57.
