# Exercise 13-8.

# If you choose words from the book at random, you can get a sense of the vocabulary,
# you probably won’t get a sentence:
# this the small regard harriet which knightley's it most things
# A series of random words seldom makes sense because there is no relationship between
# successive words. For example, in a real sentence you would expect an article like “the”
# to be followed by an adjective or a noun, and probably not a verb or adverb.
# One way to measure these kinds of relationships is Markov analysis, which characterizes,
# for a given sequence of words, the probability of the word that comes next. For example,
# the song Eric, the Half a Bee begins:

#   Half a bee, philosophically, Must, ipso facto, half not be.
#   But half the bee has got to be Vis a vis, its entity. D’you see?
#   But can a bee be said to be Or not to be an entire bee When
#   half the bee is not a bee Due to some ancient injury?

# In this text, the phrase “half the” is always followed by the word “bee,” but the phrase
# “the bee” might be followed by either “has” or “is.”
# The result of Markov analysis is a mapping from each prefix (like “half the” and “the
# bee”) to all possible suffixes (like “has” and “is”).
# Given this mapping, you can generate a random text by starting with any prefix and
# choosing at random from the possible suffixes. Next, you can combine the end of the
# prefix and the new suffix to form the next prefix, and repeat.
# For example, if you start with the prefix “Half a,” then the next word has to be “bee,”
# because the prefix only appears once in the text. The next prefix is “a bee,” so the next
# suffix might be “philosophically,” “be” or “due.”
# In this example the length of the prefix is always two, but you can do Markov analysis
# with any prefix length. The length of the prefix is called the “order” of the analysis.
# Exercise 13-8.
# Markov analysis:

# 1. Write a program to read a text from a file and perform Markov analysis. The result
# should be a dictionary that maps from prefixes to a collection of possible suffixes.
# The collection might be a list, tuple, or dictionary;
# it is up to you to make an ap propriate choice.
# You can test your program with prefix length two, but you should
# write the program in a way that makes it easy to try other lengths.

import string
import re
import random


def words_from_text(text):
    """
        Given a file, return a list of the words in the file,
        with punctuation stripped
    """
    words = []
    punctuation = re.sub('[\'.,!?]','',string.punctuation)
    fin = open(text)
    for line in fin:
        line = line.translate(
            str.maketrans(punctuation, ' ' * len(punctuation))
        )
        line = line.lower()
        line_words = line.split()
        for word in line_words:
            words.append(word)
    return words

def make_prefix_list(words,order):
    # For each word in words, create a list of tuples of each consecutive
    # n-tuple of words, according to the value of order.
    # e.g. when order = 2, given [0,1,2,3,4] return [(0,1),(1,2),(2,3),(3,4)].
    # When order=3, return [(0,1,2),(1,2,3),(2,3,4)]
    prefix_list = [
        tuple(words[i+j] for j in range(order))
        for (i, element) in enumerate(words)
        if (i+order-1) < len(words)
    ]
    return prefix_list

def make_prefix_dict(prefix_list):
    # To create a dictionary of Markov prefixes and suffixes directly from
    # this list would be inefficient, and hence prohibitively slow for large
    # texts. Instead, note that, given an n-tuple prefix A = (a1,a2,...,an),
    # the corresponding list of single suffixes can be derived by
    # taking the nth element of all n-tuple prefixes B = (b1,b2,...,bn)
    # where (a2,a3,...,an == (b1,b2,...,b(n-1)).
    # To make such a lookup as efficient as possible, we will construct
    # a dictionary where each element as of the following form:
    # (b1,b2,...,b(n-1)): bn.
    # This way, we have our matching take advantage of dictionaries' very
    # fast lookup times.
    prefix_dict = {}
    for prefix in prefix_list:
        if prefix[:-1] in prefix_dict:
            prefix_dict[prefix[:-1]].append(prefix[-1])
        else:
           prefix_dict[prefix[:-1]] = [prefix[-1]]
    return prefix_dict

def add_missing_prefixes(prefix_list,prefix_dict):
    # Now we create a dictionary composed of n-tuple prefix keys and
    # list values containing the one-word suffixes available for the given
    # n-tuple prefix. Note however that given the method used in the previous
    # step, it is possible that the last n-tuple in the text will cause an
    # error. To see this, consider the example text "Happy birthday to you",
    # and an order of 3. Our data structures are then:
    # prefix_list = [ (Happy,Birthday,to), (Birthday,to,you) ]
    # prefix_dict = {(Happy,Birthday):[to], (Birthday,to):[you]}
    # An error will occur when we try to find the possible suffixes
    # for (to, you) in prefix_dict, because there is no such key.
    # Therefore, if prefix_dict doesn't already contain a key for
    # prefix_list[-1][1:], we'll add one and give it an empty list as
    # its suffixes.
    if prefix_list[-1][1:] not in prefix_dict:
        prefix_dict[prefix_list[-1][1:]] = []
    return prefix_dict


def markov_pairs(text,order=2,additional_texts=None):
    """
    Takes text=<path to txt file> and order=<integer>, performs Markov
    analysis and returns a dictionary, the keys of which are prefix tuples
    of order <order>, and the values are lists of possible suffix words.
    An array of additional texts can be included optionally.
    For example, if given the text "To be or not to be that is the question"
    and the order=2, the function would return the following dictionary:
    {
        (to, be): [or, that],
        (be, or): [not],
        (or, not):
    }
    """
    words = words_from_text(text)
    if additional_texts:
        for additional_text in additional_texts:
            words += words_from_text(additional_text)


    prefix_list = make_prefix_list(words,order)
    prefix_dict = make_prefix_dict(prefix_list)
    prefix_dict = add_missing_prefixes(prefix_list,prefix_dict)



    pairs = {}
    for prefix in prefix_list:
        pairs[prefix] = prefix_dict[tuple(prefix[1:])]
    return pairs

# 2. Add a function to the previous program to generate random text based on the
# Markov analysis. Here is an example from Emma with prefix length 2:
# He was very clever, be it sweetness or be angry, ashamed or only amused, at such a
# stroke. She had never thought of Hannah till you were never meant for me?” “I cannot
# make speeches, Emma:” he soon cut it all himself.
# For this example, I left the punctuation attached to the words. The result is almost
# syntactically correct, but not quite. Semantically, it almost makes sense, but not
# quite.
# What happens if you increase the prefix length? Does the random text make more
# sense?

def generate_Markov_text(text,sentences=2,order=2,additional_texts=None):
    """
    Generate <sentences> sentences of Markov text of order <order>, based on
    the text in txt file <text>.
    """
    words = markov_pairs(text=text,additional_texts=additional_texts,order=order)
    sentence_count = 0
    text = []
    first_words = list(random.sample(words.keys(),1)[0])
    sentence_count += len(re.findall('[.!?]',''.join(first_words)))
    text += first_words

    while sentence_count < sentences:
        current_prefix = tuple(text[-order:])
        if len(words[current_prefix])==0:
            break
        suffix = random.sample(words[current_prefix],1)[0]
        text.append(suffix)
        sentence_count += len(re.findall('[.!?]',''.join(suffix)))

    # Capitalize words after periods, exclamation marks, or question marks.
    text[0] = text[0][:1].upper()+text[0][1:]
    for (i,word) in enumerate(text):
        if ((i-1) >= 0) and re.search("[.!?]",text[i-1]):
            text[i] = text[i][:1].upper()+text[i][1:]
    return " ".join(text)


#print(generate_Markov_text('kant_groundwork.txt',3,2))
#print("\n")

# 3. Once your program is working, you might want to try a mash-up: if you analyze
# text from two or more books, the random text you generate will blend the vocabu-
# lary and phrases from the sources in interesting ways.

#print(generate_Markov_text(text="barrister.txt",additional_texts=['fifty_shades.txt'],sentences=1,order=2))

# Kant mixed with Fifty Shades:
# "Hang up my feet. In my calendar. He swallows. Turn and seductive.
#  He groans as a categorical imperative of a trace of his name."