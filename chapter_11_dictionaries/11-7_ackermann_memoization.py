# Exercise 11-7.
# Memoize the Ackermann function from Exercise 6-5 and see if memoization makes it
# possible to evaluate the function with bigger arguments. Hint: no.
import time

ackermann_call_count = 0
memoized_ackermann_call_count = 0

# Keep track of the values of the ackermann function for various pairs
# Assign/Access as known_values[m][n]
known_values = {}

def ackermann(m, n):
    global ackermann_call_count
    ackermann_call_count += 1

    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def memoized_ackermann(m,n):
    global memoized_ackermann_call_count
    memoized_ackermann_call_count+=1

    # make a row for m in known_values if there isn't one already:
    if m not in known_values:
        known_values[m] = {}

    if n in known_values[m]:
        return known_values[m][n]

    # If we get past this point, we have a row for m, but haven't encountered
    # this n before.
    if m==0:
        result = n+1
    else:
        if n==0:
            result = memoized_ackermann(m-1,1)
        else:
            result = memoized_ackermann(m-1,memoized_ackermann(m,n-1))
    known_values[m][n] = result
    return result

ackermann_start = time.time()
result1 = ackermann(3,6)
ackermann_stop = time.time()

memoized_start = time.time()
result2 = memoized_ackermann(3,6)
memoized_stop = time.time()

print("non-memoized:",
      ackermann_call_count,
      "calls,",
      ackermann_stop - ackermann_start,
      "seconds.")

print("memoized:",
      memoized_ackermann_call_count,
      "calls,",
      memoized_stop - memoized_start,
      "seconds.")


# Memoization cuts down quite drastically on the number of function calls
# and execution time for low-valued arguments. For instance, for ackermann(3,6)
# using memoization results in 1536 calls instead of 172233, and executes in
# 0.002 seconds instead of 0.08. However, this doesn't scale, since for larger
# inputs Python chokes by recursing too deeply, so our increased performance
# doesn't amount to much in practice.
