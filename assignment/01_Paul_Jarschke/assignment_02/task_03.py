# Task 03 - Character Frequency
# Write a program that:
#    - Reads in a string and removes any spaces from the string
#    - Counts how often individual characters occur in the string
#    - Stores the information on character occurrence frequency in a dictionary
#    - Prints the dictionary.
#  If the input is “santa claus”, the output should be: {'s': 2, 'a': 3, 'n': 1, 't': 1, 'c': 1, 'l': 1, 'u': 1}.

word = input('Please enter a string:\n')

# removing all spaces
stripped = word.replace(" ", "")

# create empty dictionary
dic = {}

# add letter to dic or increase counter by 1
for i in stripped:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# print result
print(f'Dictionary output:\n {dic}')

