# Python provides a built-in function called  len that returns the length of a string, so the
# value of  len('allen') is 5.
# Write a function named  right_justify that takes a string named  s as a parameter and
# prints the string with enough leading spaces so that the last letter of the string is in
# column 70 of the display.

def right_justify(s):
    line_length = 70
    arg_length = len(s)
    print(" "*(line_length-arg_length),s,sep="")

print("         1         2         3         4         5         6         x")
print("1234567890123456789012345678901234567890123456789012345678901234567890")
right_justify("The quick brown fox jumped over the lazy dog")
