# The mathematician Srinivasa Ramanujan found an infinite series that can be used to
# generate a numerical approximation of  π :
#  1/pi = (2*sqrt(2)/9801)*sum(k=0,inf)((4k)!*(1103+26390*k))/((k!)^4*396^(4k))
# Write a function called  estimate_pi that uses this formula to compute and return an
# estimate of  π . It should use a  while loop to compute terms of the summation until the
# last term is smaller than  1e-15 (which is Python notation for 10 -15 ). You can check the
# result by comparing it to  math.pi

import math

def estimate_pi():
    k=0
    p_inv = 0
    scalar_coefficient = 2*math.sqrt(2)/9801
    while True:
        summand = 0
        summand += (math.factorial(4*k)*(1103+26390*k))
        summand /= (math.factorial(k)**4*396**(4*k))
        #break if summand < 1e-15
        if summand < 1e-15:
            break
        p_inv += scalar_coefficient*summand
        k=k+1
    return 1/p_inv

print(estimate_pi())