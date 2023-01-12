# Task 2 - List Comprehensions

# Python supports list comprehension. The basic syntax of list comprehensions is:
# L = [<elem> for <elem> <Condition>]
# Use list comprehensions to write a Python function remove_long_words() that:
#
#   -  accepts a sentence s and an integer n as input parameters
#   -  uses the split() function of String objects to split the sentence into words
#   -  stores the individual words in a list
#   -  removes all words that are longer than n characters from the list, thereby creating a new list
#   -  prints the list to stdout

# sentence input
sentence = input('Please enter a sentence: ')

# integer input
number = int(input('Please enter a positive integer: '))


def remove_long_words(s, n):
    """Removes items from input sentence that are longer than the input integer.
       Prints list with filtered words."""
    # split elements in list
    lst = s.split()
    # keep words that do have less than n letters
    out = [word for word in lst if len(word) <= n]
    # print output list to stdout
    print(f'\nYour filtered list of words:\n{out}')


# call function on input parameters
remove_long_words(sentence, number)
