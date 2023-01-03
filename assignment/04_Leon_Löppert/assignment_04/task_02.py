################################################
#### Programing for Data Scientists: Python ####
####              Assignment 04             ####
####             by Leon Löppert            ####
################################################

# Task 02 - List comprehensions ----

# Use list comprehensions to write a Python function remove_long_words() that:
#
# accepts a sentence s and an integer n as input parameters
# uses the split() function of String objects to split the sentence into words
# stores the individual words in a list
# removes all words that are longer than n characters from the list, thereby creating a new list
# prints the list to stdout

def remove_long_words(s, n):
    slist = s.split()
    outlist = [w for w in slist if len(w) <= n]
    print(outlist)

remove_long_words('Hello world. I wish yourself a wonderful day.', 5)
