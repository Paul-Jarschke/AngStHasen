# Task 03 – Character Frequency
#
# Write a program that:
#
#    Reads in a string and removes any spaces from the string
#    Counts how often individual characters occur in the string
#    Stores the information on character occurrence frequency in a dictionary
#    Prints the dictionary.
#
# For example, if the input is “santa claus”, the output should be: {'s': 2, 'a': 3, 'n': 1, 't': 1, 'c': 1, 'l': 1, 'u': 1}.

# accepting string and subsequently removing the white spaces
string_input = input("Please enter a string!\n")
string_input = string_input.strip()
helping_list = string_input.split()
string_out = ""
for x in helping_list:
    string_out += x
print(string_out)

# look for every unique char in the string how often it occurs, but skip, if it has already counted

# this set only contains chars, that havent been counted already
helping_set = set(string_out)

dic_string = ""
for char in string_out:
    if not(char in helping_set):
        continue
    helping_set = helping_set - set(char)
    dic_string = dic_string + "'" + str(char) + "':" + str(string_out.count(char)) + ", -"

# now clean the string up, so it can be cast into a dictionary
helping_list = dic_string.split(sep='-')
my_dic = "{"
for a in helping_list:
    my_dic += a
my_dic = my_dic.strip()
# print(my_dic)
my_dic = my_dic[:-1] + '}'

Dict = eval(my_dic)
print(Dict)
