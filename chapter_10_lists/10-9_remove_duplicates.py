# Exercise 10-9.
# Write a function called  remove_duplicates that takes a list and returns a new list with
# only the unique elements from the original. Hint: they don’t have to be in the same order.

def remove_duplicates(original):
    original_sorted = original[:]
    original_sorted.sort()
    output = [original_sorted[0]]
    i = 1
    while i < len(original_sorted):
        if original_sorted[i]!=original_sorted[i-1]:
            output.append(original_sorted[i])
        i+=1
    return output
print(remove_duplicates([1,2,2,2,3,3,4]))

