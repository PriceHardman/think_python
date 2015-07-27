# Exercise 12-5.
# Two words form a “metathesis pair” if you can transform one into the other by swapping
# two letters; for example, “converse” and “conserve.” Write a program that finds all of the
# metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all
# possible swaps.


def get_anagrams(word_file, count=False):
    counter = 0
    anagrams = {}
    fin = open(word_file)
    for line in fin:
        word = line.strip()
        letters = list(word)
        letters.sort()
        letters = tuple(letters)

        if letters in anagrams:
            anagrams[letters].append(word)
        else:
            anagrams[letters] = [word]

        if count == True and counter % 1000 == 0:
            print(counter)
        counter += 1
    return anagrams


def is_metathesis_pair(string1, string2):
    char_differences = 0
    for i in range(0, len(string1)):
        if string1[i] != string2[i]:
            char_differences += 1
    if char_differences == 2:
        return True
    else:
        return False

metathesis_pairs = []
anagrams = [
    val for (key, val) in get_anagrams('words.txt').items() if len(val) > 1]
n = len(anagrams)
i=0
for anagram_set in anagrams:
    for i in range(0,len(anagram_set)):
        test_word = anagram_set[i]
        possible_matches = anagram_set[i+1:]
        for possible_match in possible_matches:
            if is_metathesis_pair(test_word,possible_match):
                metathesis_pairs.append((test_word,possible_match))

for pair in metathesis_pairs:
    print(pair)
