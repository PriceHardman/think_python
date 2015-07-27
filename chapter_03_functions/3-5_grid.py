# This exercise can be done using only the statements and other features we have learned
# so far.

# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:
# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the value
# printed next appears on the same line.
# print '+',
# print '-'
# The output of these statements is  '+ -' .
# A  print statement all by itself ends the current line and goes to the next line.
def draw_grid2():
    print("+",4*" -"," +",4*" -"," +",sep="")
    print("|",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",sep="")
    print("+",4*" -"," +",4*" -"," +",sep="")
    print("|",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",sep="")
    print("+",4*" -"," +",4*" -"," +",sep="")

draw_grid2()

# 2. Write a function that draws a similar grid with four rows and four columns.
def draw_grid4():
    print("+",4*" -"," +",4*" -"," +",4*" -"," +",4*" -"," +",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("+",4*" -"," +",4*" -"," +",4*" -"," +",4*" -"," +",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("+",4*" -"," +",4*" -"," +",4*" -"," +",4*" -"," +",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("+",4*" -"," +",4*" -"," +",4*" -"," +",4*" -"," +",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("|",4*"  "," |",4*"  "," |",4*"  "," |",4*"  "," |",sep="")
    print("+",4*" -"," +",4*" -"," +",4*" -"," +",4*" -"," +",sep="")

draw_grid4()