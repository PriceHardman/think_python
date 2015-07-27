# Exercise 11-6.
# Run this version of  fibonacci and the original with a range of parameters and compare
# their run times.

import time

regular_fibonacci_count = 0
def fibonacci(n):
    global regular_fibonacci_count
    regular_fibonacci_count+=1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


memoized_fibonacci_count = 0
known_fibonacci_numbers = {0:0,1:1}
def memoized_fibonacci(n):
    global memoized_fibonacci_count
    memoized_fibonacci_count+=1
    if n in known_fibonacci_numbers:
        return known_fibonacci_numbers[n]

    result = memoized_fibonacci(n-1)+memoized_fibonacci(n-2)
    known_fibonacci_numbers[n] = result
    return result


# Measure how many calls are made to each function
# and how long each takes to run.
regular_fibonacci_start = time.time()
x = fibonacci(35)
regular_fibonacci_end = time.time()

memoized_fibonacci_start = time.time()
y = memoized_fibonacci(35)
memoized_fibonacci_end = time.time()

print("Regular Fibionacci:",
      regular_fibonacci_count,
      "calls,",
      regular_fibonacci_end - regular_fibonacci_start,
      "seconds"
      )
print("Memoized Fibonacci:",
      memoized_fibonacci_count,
      "calls",
      memoized_fibonacci_end - memoized_fibonacci_start,
      "seconds"
      )

# Regular: 29 million calls with runtime of 9 seconds
# Memoized: 69 calls, instantaneous runtime.



