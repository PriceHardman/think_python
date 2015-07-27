# Exercise 10-7.
# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called  is_anagram that takes two strings and returns  True if they are
# anagrams.


# Split word1 and word2 into lists,
# checks to see if they're anagrams of one another
# by sorting them and checking for to see if their
# letters are the same. Anagrams will have
# identical sorted lists of letters.
def is_anagram(word1, word2):
    word1_list = list(word1)
    word2_list = list(word2)
    word1_list.sort()
    word2_list.sort()

    if len(word1_list) != len(word2_list):
        return False

    i = 0
    while i < len(word1_list):
        if word1_list[i] != word2_list[i]:
            return False
        i += 1
    return True


print(is_anagram('dog','god'))
print(is_anagram('flower','tree'))
