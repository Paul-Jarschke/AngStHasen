"""
Task 02 – List comprehensions

Python supports list comprehension. The basic syntax of list comprehensions is:
L = [<elem> for <elem> <Condition>]
Use list comprehensions to write a Python function remove_long_words() that:

    accepts a sentence s and an integer n as input parameters
    uses the split() function of String objects to split the sentence into words
    stores the individual words in a list
    removes all words that are longer than n characters from the list, thereby creating a new list
    prints the list to stdout
"""


def remove_long_words(s, n):
    lst = s.split()
    lst = [x for x in lst if len(x) <= n]
    print(lst)


remove_long_words("hallo du da", 2)
