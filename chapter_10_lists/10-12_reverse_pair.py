# Exercise 10-12.
# Two words are a “reverse pair” if each is the reverse of the other. Write a program that
# finds all the reverse pairs in the word list.


def bisect(sorted_list, value):
    # index of lower bound of current interval
    lower = 0
    # index of upper bound of current interval
    upper = len(sorted_list) - 1

    while lower <= upper:
        mid = lower + int((upper - lower) / 2)
        if mid >= len(sorted_list):
            print(mid)
        mid_value = sorted_list[mid]
        if value < mid_value:
            upper = mid - 1
        elif value > mid_value:
            lower = mid + 1
        else:
            return mid              # we've found it.
    return None                     # If we haven't found it, return None

words = []
reversible_words = []
fin = open('words.txt')
for line in fin:
    words.append(line.strip())

words.sort()

for word in words:
    if (
            (bisect(words, word[::-1]) != None) and     # if reverse exists
            (word[::-1] not in reversible_words) and    # and both are new
            (word != word[::-1])                        # and not palindromes
    ):
        print(word, 'and', word[::-1])
        reversible_words.append(word)
