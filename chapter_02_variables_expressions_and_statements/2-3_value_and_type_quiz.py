# Assume that we execute the following assignment statements:
width = 17
height = 12.0
delimiter = '.'

#For each of the following expressions, write the value of the expression and the type of that value.
width/2     # => (float) 8.5
width/2.0   # => (float) 8.5
height/3    # => (float) 4.0
1+2*5       # => (int) 11
delimiter*5 # => (str) '.....'

# Check your answers:
print("width/2 =",type(width/2),width/2)
print("width/2.0",type(width/2.0),width/2.0)
print("height/3",type(height/3),height/3)
print("1+2*5",type(1+2*5),1+2*5)
print("delimiter*5",type(delimiter*5),delimiter*5)
