# Exercise 9-7.
# This question is based on a Puzzler that was broadcast on the radio program Car Talk
# (http://www.cartalk.com/content/puzzler/transcripts/200725):
# Give me a word with three consecutive double letters. I’ll give you a couple of words that
# almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It would
# be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you
# could take out those i’s it would work. But there is a word that has three consecutive pairs
# of letters and to the best of my knowledge this may be the only word. Of course there are
# probably 500 more but I can only think of one. What is the word?

def has_n_consecutive_double_letters(word,n):
    """Returns a boolean indicating if the word has n sets of consecutive doubleletters."""
    if len(word) < 2*n:
        return False

    i = 0
    while i <= (len(word) - 2*n):
        current_slice = word[i:2*n+i]
        matching_pairs_in_current_slice = 0
        j = 0

        # For the current 2*n-letter slice,
        # loop through two-by-two, checking to see if the letters
        # in each pair match one another. Keep track of how many
        # pairs match, and return True if the count reaches n.
        while j < n:
            current_pair = current_slice[j*2:j*2+2]
            if current_pair[0]==current_pair[1]:
                matching_pairs_in_current_slice += 1
            j+=1
        if matching_pairs_in_current_slice==n:
            return True
        i+=1
    return False


# See if there's a word in the file that has 3 consective double letters
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if has_n_consecutive_double_letters(word,3):
        print(word)




