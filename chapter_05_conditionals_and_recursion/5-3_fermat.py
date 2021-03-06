# Fermat’s Last Theorem says that there are no integers a, b, and c such that
#                   a^n + b^n = c^n,      for any values of n greater than 2.
#
# 1. Write a function named  check_fermat that takes four parameters— a ,  b ,  c and  n —
# and that checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns
# out to be true that a^n+b^n=c^n, the program should print, “Holy smokes, Fermat was wrong!” Otherwise the pro­
# gram should print, “No, that doesn’t work.”
def check_fermat(a,b,c,n):
    if a**n+b**n==c**n and n>2:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")


# 2. Write a function that prompts the user to input values for  a ,  b ,  c and  n , converts
# them to integers, and uses  check_fermat to check whether they violate Fermat’s
# theorem.
def get_fermat():
    print("Enter parameters for a^n+b^n=c^n:")
    a = input("a:")
    b = input("b:")
    c = input("c:")
    n = input("n:")
    check_fermat(int(a),int(b),int(c),int(n))

get_fermat()