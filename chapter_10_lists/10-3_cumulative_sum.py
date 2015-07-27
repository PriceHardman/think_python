# Exercise 10-3.
# Write a function that takes a list of numbers and returns the cumulative sum; that is, a
# new list where the ith element is the sum of the first i+1 elements from the original list.
# For example, the cumulative sum of  [1, 2, 3] is  [1, 3, 6].

def cumulative_sum(list):
    running_total = 0
    output = []
    for i in list:
        running_total+=i
        output.append(running_total)
    return output

test_list = [1,2,3,4,5]

print(cumulative_sum(test_list))
